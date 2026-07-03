import asyncio
import datetime
import logging
import os

import aiohttp
import aiostream
import uuid
import vobject
from immichpy.client.generated import PeopleResponseDto, PeopleUpdateDto, \
    PeopleUpdateItem, BulkIdResponseDto

from vdirsyncer.cli import fetchparams
from vdirsyncer.storage import dav
from vdirsyncer.vobject import Item

from immichpy import AsyncClient

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
        contacts = []
        for _, item, _ in card_contacts:
            vcard = vobject.readOne(item.raw)

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

                contacts.append({
                    "birthday": formatted_birthday,
                    "fields": {
                        # Order is important here: it also defines the priority for name matching.
                        # Starting Python 3.7 dict has guaranteed insertion order.
                        "fn": fn,
                        "first_last": first_last,
                        "nickname": nickname
                    }
                })

            except ValueError:
                # invalid date
                pass
            except AttributeError:
                # BDAY doesn't exist
                pass

        return contacts

async def fetch_immich_people(api_url: str, api_key: str):
    """
    Fetches people data from Immich.
    :return: a dict having person names as key and a list of (person_id, birth_date) as values
    """
    async with AsyncClient(base_url=api_url, api_key=api_key) as client:
        people: PeopleResponseDto = await client.people.get_all_people()
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


async def set_immich_birth_date(person_id: uuid.UUID, birth_date: str, api_url: str, api_key: str):
    logger.debug('PUT /people/%s << {"birthDate":"%s"}', person_id, birth_date)
    async with AsyncClient(base_url=api_url, api_key=api_key) as client:
        dto = PeopleUpdateDto(people=[PeopleUpdateItem(birthDate=datetime.date.fromisoformat(birth_date),
                                                       id=person_id)])
        response: list[BulkIdResponseDto] = await client.people.update_people(dto)
        if not response or len(response) < 1 or not response[0].success:
            raise RuntimeError("Birth date was not set.")

def match_person_to_first_contact(person_name: str, contacts: list) -> dict|None:
    """
    Match a person name in Immich to the first contact that it can find in the address book.
    :return: the first matched contact, otherwise None.
    """

    logger.debug("Search for %s in contacts", person_name)
    for contact in contacts:
        logger.debug("Checking contact: %s", contact)
        for field, value in contact["fields"].items():
            if value == person_name:
                logger.debug("Found matching person by %s: %s", field.replace('_', ' '), person_name)
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

    for person_name, people_data in people.items():
        logger.debug("Processing person: %s", person_name)
        match = match_person_to_first_contact(person_name, addressbook)
        if match:
            for person in people_data:
                # people with same name will have same date of birth
                if match["birthday"] != person[1]:
                    logger.info("Found matching contact for %s (%s): %s", person_name, person[0], match['birthday'])
                    await set_immich_birth_date(
                        person[0], match['birthday'], settings.immich_api_url, settings.immich_api_key
                    )
                else:
                    logger.info("Birth date for person %s (%s) is already %s - skipping" %
                                (person_name, person[0], match['birthday']))

        else:
            logger.info("Person %s not found in contacts - skipping" % person_name)


def main():
    # FIXME I don't like this
    log_level = logging.getLevelName(os.getenv("LOG_LEVEL"))
    if type(log_level) != int:
        log_level = logging.INFO
    init_logging(log_level)

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
