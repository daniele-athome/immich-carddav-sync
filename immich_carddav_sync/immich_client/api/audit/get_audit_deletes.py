import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_deletes_response_dto import AuditDeletesResponseDto
from ...models.entity_type import EntityType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: datetime.datetime,
    entity_type: EntityType,
    user_id: Union[Unset, UUID] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_after = after.isoformat()
    params["after"] = json_after

    json_entity_type = entity_type.value
    params["entityType"] = json_entity_type

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/audit/deletes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuditDeletesResponseDto]:
    if response.status_code == 200:
        response_200 = AuditDeletesResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuditDeletesResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after: datetime.datetime,
    entity_type: EntityType,
    user_id: Union[Unset, UUID] = UNSET,
) -> Response[AuditDeletesResponseDto]:
    """
    Args:
        after (datetime.datetime):
        entity_type (EntityType):
        user_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditDeletesResponseDto]
    """

    kwargs = _get_kwargs(
        after=after,
        entity_type=entity_type,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    after: datetime.datetime,
    entity_type: EntityType,
    user_id: Union[Unset, UUID] = UNSET,
) -> Optional[AuditDeletesResponseDto]:
    """
    Args:
        after (datetime.datetime):
        entity_type (EntityType):
        user_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditDeletesResponseDto
    """

    return sync_detailed(
        client=client,
        after=after,
        entity_type=entity_type,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: datetime.datetime,
    entity_type: EntityType,
    user_id: Union[Unset, UUID] = UNSET,
) -> Response[AuditDeletesResponseDto]:
    """
    Args:
        after (datetime.datetime):
        entity_type (EntityType):
        user_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditDeletesResponseDto]
    """

    kwargs = _get_kwargs(
        after=after,
        entity_type=entity_type,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after: datetime.datetime,
    entity_type: EntityType,
    user_id: Union[Unset, UUID] = UNSET,
) -> Optional[AuditDeletesResponseDto]:
    """
    Args:
        after (datetime.datetime):
        entity_type (EntityType):
        user_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditDeletesResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            entity_type=entity_type,
            user_id=user_id,
        )
    ).parsed
