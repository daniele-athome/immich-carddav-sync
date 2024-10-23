from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_id_response_dto import BulkIdResponseDto
from ...models.bulk_ids_dto import BulkIdsDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    json_body: BulkIdsDto,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/album/{id}/assets".format(
            id=id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["BulkIdResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BulkIdResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["BulkIdResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: BulkIdsDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[List["BulkIdResponseDto"]]:
    """
    Args:
        id (str):
        key (Union[Unset, None, str]):
        json_body (BulkIdsDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BulkIdResponseDto']]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: BulkIdsDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[List["BulkIdResponseDto"]]:
    """
    Args:
        id (str):
        key (Union[Unset, None, str]):
        json_body (BulkIdsDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BulkIdResponseDto']
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        key=key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: BulkIdsDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[List["BulkIdResponseDto"]]:
    """
    Args:
        id (str):
        key (Union[Unset, None, str]):
        json_body (BulkIdsDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BulkIdResponseDto']]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: BulkIdsDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[List["BulkIdResponseDto"]]:
    """
    Args:
        id (str):
        key (Union[Unset, None, str]):
        json_body (BulkIdsDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BulkIdResponseDto']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            key=key,
        )
    ).parsed
