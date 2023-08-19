#!/usr/bin/env python3

import asyncio
import datetime
import sys

import aiohttp
import aiostream
import vobject
from vdirsyncer.cli import fetchparams
from vdirsyncer.storage import dav
from vdirsyncer.vobject import Item


async def main(argv):
    async with aiohttp.TCPConnector(limit_per_host=16) as conn:
        collection_name = argv[3]
        config = {
            'connector': conn,
            'url': argv[1],
            'username': argv[2],
            'password.fetch': ["command", "keyring", "-b", "keyring.backends.SecretService.Keyring", "get",
                               "vdirsyncer", argv[2]],
        }
        config = fetchparams.expand_fetch_params(config)
        client = dav.CardDAVStorage(**config)
        collection = await aiostream.stream.filter(client.discover(**config),
                                                   lambda x: x['collection'] == collection_name)
        print(collection)

        config['url'] = collection['url']
        client = dav.CardDAVStorage(**config)
        discovered = await aiostream.stream.list(client.list())
        # print(discovered)

        hrefs = [x[0] for x in discovered]
        contacts = await aiostream.stream.list(client.get_multi(hrefs))
        # print(contacts)
        item: Item
        for (_, item, _) in contacts:
            vcard = vobject.readOne(item.raw)
            try:
                bday = datetime.date.fromisoformat(vcard.bday.value)
                print(bday)

            except ValueError:
                # invalid date
                pass
            except AttributeError:
                # BDAY doesn't exist
                pass

        import code
        code.interact(local=locals())


asyncio.run(main(sys.argv))
