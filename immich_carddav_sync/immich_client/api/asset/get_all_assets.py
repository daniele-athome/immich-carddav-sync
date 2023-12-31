from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_response_dto import AssetResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    without_thumbs: Union[Unset, None, bool] = UNSET,
    skip: Union[Unset, None, float] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(if_none_match, Unset):
        headers["if-none-match"] = if_none_match

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["isFavorite"] = is_favorite

    params["isArchived"] = is_archived

    params["withoutThumbs"] = without_thumbs

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset",
        "params": params,
        "headers": headers,
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
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    without_thumbs: Union[Unset, None, bool] = UNSET,
    skip: Union[Unset, None, float] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """Get all AssetEntity belong to the user

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        without_thumbs (Union[Unset, None, bool]):
        skip (Union[Unset, None, float]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        is_favorite=is_favorite,
        is_archived=is_archived,
        without_thumbs=without_thumbs,
        skip=skip,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    without_thumbs: Union[Unset, None, bool] = UNSET,
    skip: Union[Unset, None, float] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """Get all AssetEntity belong to the user

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        without_thumbs (Union[Unset, None, bool]):
        skip (Union[Unset, None, float]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        is_favorite=is_favorite,
        is_archived=is_archived,
        without_thumbs=without_thumbs,
        skip=skip,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    without_thumbs: Union[Unset, None, bool] = UNSET,
    skip: Union[Unset, None, float] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """Get all AssetEntity belong to the user

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        without_thumbs (Union[Unset, None, bool]):
        skip (Union[Unset, None, float]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        is_favorite=is_favorite,
        is_archived=is_archived,
        without_thumbs=without_thumbs,
        skip=skip,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    without_thumbs: Union[Unset, None, bool] = UNSET,
    skip: Union[Unset, None, float] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """Get all AssetEntity belong to the user

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        without_thumbs (Union[Unset, None, bool]):
        skip (Union[Unset, None, float]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            is_favorite=is_favorite,
            is_archived=is_archived,
            without_thumbs=without_thumbs,
            skip=skip,
            if_none_match=if_none_match,
        )
    ).parsed
