from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_order import AssetOrder
from ...models.time_bucket_response_dto import TimeBucketResponseDto
from ...models.time_bucket_size import TimeBucketSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    album_id: Union[Unset, UUID] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    order: Union[Unset, AssetOrder] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    size: TimeBucketSize,
    tag_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_stacked: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_album_id: Union[Unset, str] = UNSET
    if not isinstance(album_id, Unset):
        json_album_id = str(album_id)
    params["albumId"] = json_album_id

    params["isArchived"] = is_archived

    params["isFavorite"] = is_favorite

    params["isTrashed"] = is_trashed

    params["key"] = key

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    json_size = size.value
    params["size"] = json_size

    json_tag_id: Union[Unset, str] = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = str(tag_id)
    params["tagId"] = json_tag_id

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["withPartners"] = with_partners

    params["withStacked"] = with_stacked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/timeline/buckets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["TimeBucketResponseDto"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TimeBucketResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["TimeBucketResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album_id: Union[Unset, UUID] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    order: Union[Unset, AssetOrder] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    size: TimeBucketSize,
    tag_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_stacked: Union[Unset, bool] = UNSET,
) -> Response[List["TimeBucketResponseDto"]]:
    """
    Args:
        album_id (Union[Unset, UUID]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):
        key (Union[Unset, str]):
        order (Union[Unset, AssetOrder]):
        person_id (Union[Unset, UUID]):
        size (TimeBucketSize):
        tag_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        with_partners (Union[Unset, bool]):
        with_stacked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TimeBucketResponseDto']]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        size=size,
        tag_id=tag_id,
        user_id=user_id,
        with_partners=with_partners,
        with_stacked=with_stacked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album_id: Union[Unset, UUID] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    order: Union[Unset, AssetOrder] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    size: TimeBucketSize,
    tag_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_stacked: Union[Unset, bool] = UNSET,
) -> Optional[List["TimeBucketResponseDto"]]:
    """
    Args:
        album_id (Union[Unset, UUID]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):
        key (Union[Unset, str]):
        order (Union[Unset, AssetOrder]):
        person_id (Union[Unset, UUID]):
        size (TimeBucketSize):
        tag_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        with_partners (Union[Unset, bool]):
        with_stacked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TimeBucketResponseDto']
    """

    return sync_detailed(
        client=client,
        album_id=album_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        size=size,
        tag_id=tag_id,
        user_id=user_id,
        with_partners=with_partners,
        with_stacked=with_stacked,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album_id: Union[Unset, UUID] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    order: Union[Unset, AssetOrder] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    size: TimeBucketSize,
    tag_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_stacked: Union[Unset, bool] = UNSET,
) -> Response[List["TimeBucketResponseDto"]]:
    """
    Args:
        album_id (Union[Unset, UUID]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):
        key (Union[Unset, str]):
        order (Union[Unset, AssetOrder]):
        person_id (Union[Unset, UUID]):
        size (TimeBucketSize):
        tag_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        with_partners (Union[Unset, bool]):
        with_stacked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TimeBucketResponseDto']]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
        key=key,
        order=order,
        person_id=person_id,
        size=size,
        tag_id=tag_id,
        user_id=user_id,
        with_partners=with_partners,
        with_stacked=with_stacked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album_id: Union[Unset, UUID] = UNSET,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
    key: Union[Unset, str] = UNSET,
    order: Union[Unset, AssetOrder] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    size: TimeBucketSize,
    tag_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    with_partners: Union[Unset, bool] = UNSET,
    with_stacked: Union[Unset, bool] = UNSET,
) -> Optional[List["TimeBucketResponseDto"]]:
    """
    Args:
        album_id (Union[Unset, UUID]):
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):
        key (Union[Unset, str]):
        order (Union[Unset, AssetOrder]):
        person_id (Union[Unset, UUID]):
        size (TimeBucketSize):
        tag_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        with_partners (Union[Unset, bool]):
        with_stacked (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['TimeBucketResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            size=size,
            tag_id=tag_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
        )
    ).parsed
