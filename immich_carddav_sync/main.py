import asyncio
import datetime
import logging
import os

import aiohttp
import aiostream
import vobject

from vdirsyncer.cli import fetchparams
from vdirsyncer.storage import dav
from vdirsyncer.vobject import Item

from .immich_client import AuthenticatedClient
from .immich_client.api.person import get_all_people, update_person
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
        contacts = await aiostream.stream.list(client.get_multi(hrefs))

        item: Item
        names = {}
        for _, item, _ in contacts:
            vcard = vobject.readOne(item.raw)
            try:
                names[vcard.fn.value] = datetime.date.fromisoformat(vcard.bday.value).isoformat()
            except ValueError:
                # invalid date
                pass
            except AttributeError:
                # BDAY doesn't exist
                pass

        return names


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
                names[person.name] = (person.id, birth_date)
        return names


async def set_immich_birth_date(person_id: str, birth_date: str, api_url: str, api_key: str):
    logger.debug('PUT /people/%s << {"birthDate":"%s"}', person_id, birth_date)
    with AuthenticatedClient(base_url=api_url, auth_header_name="X-api-key", prefix="", token=api_key) as client:
        dto = PersonUpdateDto(birth_date=datetime.date.fromisoformat(birth_date))
        response: PersonResponseDto = await update_person.asyncio(id=person_id, json_body=dto, client=client)
        if not response or response.birth_date.isoformat() != birth_date:
            raise RuntimeError("Birth date was not set.")


async def async_main():
    logger.info("Fetching CardDAV address book...")
    addressbook = await fetch_carddav_addressbook(
        settings.carddav_url, settings.carddav_addressbook, settings.carddav_username, settings.carddav_password
    )
    logger.debug(addressbook)

    logger.info("Fetching people from Immich...")
    people = await fetch_immich_people(settings.immich_api_url, settings.immich_api_key)
    logger.debug(people)

    for contact_name, contact_bday in addressbook.items():
        if contact_name in people:
            if contact_bday != people[contact_name][1]:
                logger.info("Setting birth date for %s to %s" % (contact_name, contact_bday))
                await set_immich_birth_date(
                    people[contact_name][0], contact_bday, settings.immich_api_url, settings.immich_api_key
                )
            else:
                logger.info("Birth date for %s is already %s - skipping" % (contact_name, contact_bday))
        else:
            logger.info("Contact %s not found in Immich - skipping" % contact_name)


def main():
    # FIXME I don't like this
    log_level = logging.getLevelName(os.getenv("LOG_LEVEL"))
    if type(log_level) != int:
        log_level = logging.INFO
    init_logging(log_level)

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
