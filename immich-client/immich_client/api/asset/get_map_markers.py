import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.map_marker_response_dto import MapMarkerResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_favorite: Union[Unset, None, bool] = UNSET,
    file_created_after: Union[Unset, None, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["isFavorite"] = is_favorite

    json_file_created_after: Union[Unset, None, str] = UNSET
    if not isinstance(file_created_after, Unset):
        json_file_created_after = file_created_after.isoformat() if file_created_after else None

    params["fileCreatedAfter"] = json_file_created_after

    json_file_created_before: Union[Unset, None, str] = UNSET
    if not isinstance(file_created_before, Unset):
        json_file_created_before = file_created_before.isoformat() if file_created_before else None

    params["fileCreatedBefore"] = json_file_created_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset/map-marker",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["MapMarkerResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MapMarkerResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["MapMarkerResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_favorite: Union[Unset, None, bool] = UNSET,
    file_created_after: Union[Unset, None, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[List["MapMarkerResponseDto"]]:
    """
    Args:
        is_favorite (Union[Unset, None, bool]):
        file_created_after (Union[Unset, None, datetime.datetime]):
        file_created_before (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapMarkerResponseDto']]
    """

    kwargs = _get_kwargs(
        is_favorite=is_favorite,
        file_created_after=file_created_after,
        file_created_before=file_created_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_favorite: Union[Unset, None, bool] = UNSET,
    file_created_after: Union[Unset, None, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[List["MapMarkerResponseDto"]]:
    """
    Args:
        is_favorite (Union[Unset, None, bool]):
        file_created_after (Union[Unset, None, datetime.datetime]):
        file_created_before (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapMarkerResponseDto']
    """

    return sync_detailed(
        client=client,
        is_favorite=is_favorite,
        file_created_after=file_created_after,
        file_created_before=file_created_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_favorite: Union[Unset, None, bool] = UNSET,
    file_created_after: Union[Unset, None, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[List["MapMarkerResponseDto"]]:
    """
    Args:
        is_favorite (Union[Unset, None, bool]):
        file_created_after (Union[Unset, None, datetime.datetime]):
        file_created_before (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapMarkerResponseDto']]
    """

    kwargs = _get_kwargs(
        is_favorite=is_favorite,
        file_created_after=file_created_after,
        file_created_before=file_created_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_favorite: Union[Unset, None, bool] = UNSET,
    file_created_after: Union[Unset, None, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[List["MapMarkerResponseDto"]]:
    """
    Args:
        is_favorite (Union[Unset, None, bool]):
        file_created_after (Union[Unset, None, datetime.datetime]):
        file_created_before (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapMarkerResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            is_favorite=is_favorite,
            file_created_after=file_created_after,
            file_created_before=file_created_before,
        )
    ).parsed
