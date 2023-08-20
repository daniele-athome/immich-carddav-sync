#!/usr/bin/env python3

import sys

from immich_client import AuthenticatedClient
from immich_client.api.person import get_person
from immich_client.models import PersonResponseDto
from immich_client.types import Response

client = AuthenticatedClient(
    base_url=sys.argv[1], auth_header_name="X-api-key", prefix="", token=sys.argv[2]
)

with client as client:
    person: PersonResponseDto = get_person.sync(
        id="7530340a-5c92-49a0-8044-66ab44b2deba", client=client
    )
    print(person)
    # or if you need more info (e.g. status_code)
    response: Response[PersonResponseDto] = get_person.sync_detailed(
        id="7530340a-5c92-49a0-8044-66ab44b2deba", client=client
    )
    print(response)
