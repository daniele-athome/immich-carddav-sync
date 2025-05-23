from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_stats_response_dto import AssetStatsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["isArchived"] = is_archived

    params["isFavorite"] = is_favorite

    params["isTrashed"] = is_trashed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/assets/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetStatsResponseDto]:
    if response.status_code == 200:
        response_200 = AssetStatsResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetStatsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
) -> Response[AssetStatsResponseDto]:
    """
    Args:
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetStatsResponseDto]
    """

    kwargs = _get_kwargs(
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
) -> Optional[AssetStatsResponseDto]:
    """
    Args:
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetStatsResponseDto
    """

    return sync_detailed(
        client=client,
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
) -> Response[AssetStatsResponseDto]:
    """
    Args:
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetStatsResponseDto]
    """

    kwargs = _get_kwargs(
        is_archived=is_archived,
        is_favorite=is_favorite,
        is_trashed=is_trashed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_archived: Union[Unset, bool] = UNSET,
    is_favorite: Union[Unset, bool] = UNSET,
    is_trashed: Union[Unset, bool] = UNSET,
) -> Optional[AssetStatsResponseDto]:
    """
    Args:
        is_archived (Union[Unset, bool]):
        is_favorite (Union[Unset, bool]):
        is_trashed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetStatsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
        )
    ).parsed
