import asyncio
import datetime

import aiohttp
import aiostream
import vobject

from vdirsyncer.cli import fetchparams
from vdirsyncer.storage import dav
from vdirsyncer.vobject import Item

from .immich_client import AuthenticatedClient
from .immich_client.api.person import get_all_people
from .immich_client.models import PeopleResponseDto


from .config import settings


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


async def async_main():
    addressbook = await fetch_carddav_addressbook(
        settings.carddav_url, settings.carddav_addressbook, settings.carddav_username, settings.carddav_password
    )
    print(addressbook)
    people = await fetch_immich_people(settings.immich_api_url, settings.immich_api_key)
    print(people)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
