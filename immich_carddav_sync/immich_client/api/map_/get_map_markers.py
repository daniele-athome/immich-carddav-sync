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
    file_created_after: Union[Unset, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, datetime.datetime] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_shared_albums: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_file_created_after: Union[Unset, str] = UNSET
    if not isinstance(file_created_after, Unset):
        json_file_created_after = file_created_after.isoformat()
    params["fileCreatedAfter"] = json_file_created_after

    json_file_created_before: Union[Unset, str] = UNSET
    if not isinstance(file_created_before, Unset):
        json_file_created_before = file_created_before.isoformat()
    params["fileCreatedBefore"] = json_file_created_before

    params["isArchived"] = is_archived

    params["isFavorite"] = is_favorite

    params["withPartners"] = with_partners

    params["withSharedAlbums"] = with_shared_albums

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/map/markers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["MapMarkerResponseDto"]]:
    if response.status_code == 200:
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
    file_created_after: Union[Unset, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, datetime.datetime] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_shared_albums: Union[Unset, bool] = UNSET,
) -> Response[List["MapMarkerResponseDto"]]:
    """
    Args:
        file_created_after (Union[Unset, datetime.datetime]):
        file_created_before (Union[Unset, datetime.datetime]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        with_partners (Union[Unset, bool]):
        with_shared_albums (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapMarkerResponseDto']]
    """

    kwargs = _get_kwargs(
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    file_created_after: Union[Unset, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, datetime.datetime] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_shared_albums: Union[Unset, bool] = UNSET,
) -> Optional[List["MapMarkerResponseDto"]]:
    """
    Args:
        file_created_after (Union[Unset, datetime.datetime]):
        file_created_before (Union[Unset, datetime.datetime]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        with_partners (Union[Unset, bool]):
        with_shared_albums (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapMarkerResponseDto']
    """

    return sync_detailed(
        client=client,
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    file_created_after: Union[Unset, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, datetime.datetime] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_shared_albums: Union[Unset, bool] = UNSET,
) -> Response[List["MapMarkerResponseDto"]]:
    """
    Args:
        file_created_after (Union[Unset, datetime.datetime]):
        file_created_before (Union[Unset, datetime.datetime]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        with_partners (Union[Unset, bool]):
        with_shared_albums (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapMarkerResponseDto']]
    """

    kwargs = _get_kwargs(
        file_created_after=file_created_after,
        file_created_before=file_created_before,
        is_archived=is_archived,
        is_favorite=is_favorite,
        with_partners=with_partners,
        with_shared_albums=with_shared_albums,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    file_created_after: Union[Unset, datetime.datetime] = UNSET,
    file_created_before: Union[Unset, datetime.datetime] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_shared_albums: Union[Unset, bool] = UNSET,
) -> Optional[List["MapMarkerResponseDto"]]:
    """
    Args:
        file_created_after (Union[Unset, datetime.datetime]):
        file_created_before (Union[Unset, datetime.datetime]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        with_partners (Union[Unset, bool]):
        with_shared_albums (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapMarkerResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            file_created_after=file_created_after,
            file_created_before=file_created_before,
            is_archived=is_archived,
            is_favorite=is_favorite,
            with_partners=with_partners,
            with_shared_albums=with_shared_albums,
        )
    ).parsed
