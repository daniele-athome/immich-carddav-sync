import asyncio
import datetime
import logging
import os

import aiohttp
import aiostream
import uuid
import vobject

from vdirsyncer.cli import fetchparams
from vdirsyncer.storage import dav
from vdirsyncer.vobject import Item

from .immich_client import AuthenticatedClient
from .immich_client.api.people import get_all_people, update_person
from .immich_client.models import PeopleResponseDto, PersonResponseDto, PersonUpdateDto


from .config import settings
from .logger import init_logging


logger = logging.getLogger("immich-carddav-sync")


async def fetch_carddav_addressbook(url: str, collection: str, username: str, password: str):
    async with aiohttp.TCPConnector(limit_per_host=16) as conn:
        config = {
            "connector": conn,
            "url": url,
            "username": username,
            "password": password,
        }
        config = fetchparams.expand_fetch_params(config)
        client = dav.CardDAVStorage(**config)
        collection = await aiostream.stream.filter(client.discover(**config), lambda x: x["collection"] == collection)

        config["url"] = collection["url"]
        client = dav.CardDAVStorage(**config)
        discovered = await aiostream.stream.list(client.list())

        hrefs = [x[0] for x in discovered]
        card_contacts = await aiostream.stream.list(client.get_multi(hrefs))

        item: Item
        contacts = {}
        for _, item, _ in card_contacts:
            vcard = vobject.readOne(item.raw)

            if hasattr(vcard, "uid") and vcard.uid.value:
                id = vcard.uid.value
            elif hasattr(vcard, "fn") and vcard.fn.value:
                # if the vcard has a fn, use it as ID
                id = vcard.fn.value
            else:
                logger.warning("No ID found for vCard: %s", item.raw)
                continue  # skip if no ID can be determined

            logger.debug("Processing contact: %s", id)
            if id in contacts:
                # duplicate contact name - currently not handled
                raise NotImplementedError('Duplicate contacts cannot be handled yet ("%s").' % id)

            try:
                birthday = datetime.date.fromisoformat(vcard.bday.value)
                try:
                    omit_year = vcard.bday.params["X-APPLE-OMIT-YEAR"][0]
                    if str(birthday.year) == omit_year:
                        # birthday without year, skip
                        raise ValueError
                except (KeyError, IndexError):
                    # no omit year, all fine!
                    pass


                first_last = None
                if hasattr(vcard, "n") and vcard.n.value:
                    # use the first and last name from the vcard
                    if hasattr(vcard.n.value, "given") and hasattr(vcard.n.value, "family"):
                        first_last = f"{vcard.n.value.given} {vcard.n.value.family}".strip()
                        
                formatted_birthday = birthday.isoformat()

                fn = None
                if hasattr(vcard, "fn") and vcard.fn.value:
                    # use the formatted name from the vcard
                    fn = vcard.fn.value.strip()
                
                nickname = None
                if hasattr(vcard, "nickname") and vcard.nickname.value:
                    # use the nickname from the vcard
                    nickname = vcard.nickname.value.strip()

                contacts[id] = {
                    "birthday": formatted_birthday,
                    "fn": fn,
                    "first_last": first_last,
                    "nickname": nickname
                }

            except ValueError:
                # invalid date
                pass
            except AttributeError:
                # BDAY doesn't exist
                pass

        return contacts

async def fetch_immich_people(api_url: str, api_key: str):
    with AuthenticatedClient(base_url=api_url, auth_header_name="X-api-key", prefix="", token=api_key) as client:
        people: PeopleResponseDto = await get_all_people.asyncio(client=client)
        names = {}
        for person in people.people:
            if person.name and len(person.name.strip()) > 0:
                if person.birth_date:
                    birth_date = person.birth_date.isoformat()
                else:
                    birth_date = None

                if person.name not in names:
                    names[person.name] = []

                # duplicates will have the same date of birth
                names[person.name].append((person.id, birth_date))

        return names


async def set_immich_birth_date(person_id: str, birth_date: str, api_url: str, api_key: str):
    logger.debug('PUT /people/%s << {"birthDate":"%s"}', person_id, birth_date)
    with AuthenticatedClient(base_url=api_url, auth_header_name="X-api-key", prefix="", token=api_key) as client:
        dto = PersonUpdateDto(birth_date=datetime.date.fromisoformat(birth_date))
        response: PersonResponseDto = await update_person.asyncio(id=uuid.UUID(person_id), body=dto, client=client)
        if not response or response.birth_date.isoformat() != birth_date:
            raise RuntimeError("Birth date was not set.")

def match_person_to_contact(person: tuple, contacts: dict):
    """
    Match a person in Immich to a contact in the address book.
    Returns the contact if a match is found, otherwise None.
    The person is a tuple of (name, [(id, birth_date)]).
    """
    name = person[0]
    
    # Fields to check for a match, in order of priority.
    match_fields = ["fn", "first_last", "nickname"]

    logger.debug("Checking in contacts %s", contacts)
    for _, contact in contacts.items():
        logger.debug("Checking contact: %s", contact)
        for field in match_fields:
            if contact.get(field) == name:
                logger.debug("Found matching person by %s: %s", field.replace('_', ' '), name)
                return contact

    return None

async def async_main():
    logger.info("Fetching CardDAV address book...")
    addressbook = await fetch_carddav_addressbook(
        settings.carddav_url, settings.carddav_addressbook, settings.carddav_username, settings.carddav_password
    )
    logger.debug(addressbook)

    logger.info("Fetching people from Immich...")
    people = await fetch_immich_people(settings.immich_api_url, settings.immich_api_key)
    logger.debug(people)

    for person in people.items():
        logger.debug("Processing person: %s", person)
        match = await match_person_to_contact(person, addressbook)
        if match:
            if match["birthday"] != person[1][0][1]:
                logger.info("Found matching contact for %s: %s", person[0], match)
                await set_immich_birth_date(
                    person[1][0][0], match['birthday'], settings.immich_api_url, settings.immich_api_key
                )
            else:
                logger.info("Birth date for %s is already %s - skipping" % (match['fn'], match['birthday']))

        else:
            logger.info("Person %s not found in Contacts - skipping" % (person[0]))


def main():
    # FIXME I don't like this
    log_level = logging.getLevelName(os.getenv("LOG_LEVEL"))
    if type(log_level) != int:
        log_level = logging.INFO
    init_logging(log_level)

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
