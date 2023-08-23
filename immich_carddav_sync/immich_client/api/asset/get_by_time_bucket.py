from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_response_dto import AssetResponseDto
from ...models.time_bucket_size import TimeBucketSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    size: TimeBucketSize,
    user_id: Union[Unset, None, str] = UNSET,
    album_id: Union[Unset, None, str] = UNSET,
    person_id: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    time_bucket: str,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_size = size.value

    params["size"] = json_size

    params["userId"] = user_id

    params["albumId"] = album_id

    params["personId"] = person_id

    params["isArchived"] = is_archived

    params["isFavorite"] = is_favorite

    params["timeBucket"] = time_bucket

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset/time-bucket",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AssetResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssetResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AssetResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    size: TimeBucketSize,
    user_id: Union[Unset, None, str] = UNSET,
    album_id: Union[Unset, None, str] = UNSET,
    person_id: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    time_bucket: str,
    key: Union[Unset, None, str] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """
    Args:
        size (TimeBucketSize):
        user_id (Union[Unset, None, str]):
        album_id (Union[Unset, None, str]):
        person_id (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        time_bucket (str):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        size=size,
        user_id=user_id,
        album_id=album_id,
        person_id=person_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        time_bucket=time_bucket,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    size: TimeBucketSize,
    user_id: Union[Unset, None, str] = UNSET,
    album_id: Union[Unset, None, str] = UNSET,
    person_id: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    time_bucket: str,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """
    Args:
        size (TimeBucketSize):
        user_id (Union[Unset, None, str]):
        album_id (Union[Unset, None, str]):
        person_id (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        time_bucket (str):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return sync_detailed(
        client=client,
        size=size,
        user_id=user_id,
        album_id=album_id,
        person_id=person_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        time_bucket=time_bucket,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    size: TimeBucketSize,
    user_id: Union[Unset, None, str] = UNSET,
    album_id: Union[Unset, None, str] = UNSET,
    person_id: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    time_bucket: str,
    key: Union[Unset, None, str] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """
    Args:
        size (TimeBucketSize):
        user_id (Union[Unset, None, str]):
        album_id (Union[Unset, None, str]):
        person_id (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        time_bucket (str):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        size=size,
        user_id=user_id,
        album_id=album_id,
        person_id=person_id,
        is_archived=is_archived,
        is_favorite=is_favorite,
        time_bucket=time_bucket,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    size: TimeBucketSize,
    user_id: Union[Unset, None, str] = UNSET,
    album_id: Union[Unset, None, str] = UNSET,
    person_id: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    time_bucket: str,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """
    Args:
        size (TimeBucketSize):
        user_id (Union[Unset, None, str]):
        album_id (Union[Unset, None, str]):
        person_id (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        time_bucket (str):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
            user_id=user_id,
            album_id=album_id,
            person_id=person_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            time_bucket=time_bucket,
            key=key,
        )
    ).parsed
