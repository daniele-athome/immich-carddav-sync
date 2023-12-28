import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_deletes_response_dto import AuditDeletesResponseDto
from ...models.entity_type import EntityType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    entity_type: EntityType,
    user_id: Union[Unset, None, str] = UNSET,
    after: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_entity_type = entity_type.value

    params["entityType"] = json_entity_type

    params["userId"] = user_id

    json_after = after.isoformat()

    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/audit/deletes",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuditDeletesResponseDto]:
    if response.status_code == HTTPStatus.OK:
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
    entity_type: EntityType,
    user_id: Union[Unset, None, str] = UNSET,
    after: datetime.datetime,
) -> Response[AuditDeletesResponseDto]:
    """
    Args:
        entity_type (EntityType):
        user_id (Union[Unset, None, str]):
        after (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditDeletesResponseDto]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        user_id=user_id,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    entity_type: EntityType,
    user_id: Union[Unset, None, str] = UNSET,
    after: datetime.datetime,
) -> Optional[AuditDeletesResponseDto]:
    """
    Args:
        entity_type (EntityType):
        user_id (Union[Unset, None, str]):
        after (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditDeletesResponseDto
    """

    return sync_detailed(
        client=client,
        entity_type=entity_type,
        user_id=user_id,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    entity_type: EntityType,
    user_id: Union[Unset, None, str] = UNSET,
    after: datetime.datetime,
) -> Response[AuditDeletesResponseDto]:
    """
    Args:
        entity_type (EntityType):
        user_id (Union[Unset, None, str]):
        after (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditDeletesResponseDto]
    """

    kwargs = _get_kwargs(
        entity_type=entity_type,
        user_id=user_id,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    entity_type: EntityType,
    user_id: Union[Unset, None, str] = UNSET,
    after: datetime.datetime,
) -> Optional[AuditDeletesResponseDto]:
    """
    Args:
        entity_type (EntityType):
        user_id (Union[Unset, None, str]):
        after (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditDeletesResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            entity_type=entity_type,
            user_id=user_id,
            after=after,
        )
    ).parsed
