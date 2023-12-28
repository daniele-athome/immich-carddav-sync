from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_statistics_response_dto import ActivityStatisticsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    album_id: str,
    asset_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["albumId"] = album_id

    params["assetId"] = asset_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/activity/statistics",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ActivityStatisticsResponseDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActivityStatisticsResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ActivityStatisticsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album_id: str,
    asset_id: Union[Unset, None, str] = UNSET,
) -> Response[ActivityStatisticsResponseDto]:
    """
    Args:
        album_id (str):
        asset_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityStatisticsResponseDto]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album_id: str,
    asset_id: Union[Unset, None, str] = UNSET,
) -> Optional[ActivityStatisticsResponseDto]:
    """
    Args:
        album_id (str):
        asset_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityStatisticsResponseDto
    """

    return sync_detailed(
        client=client,
        album_id=album_id,
        asset_id=asset_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album_id: str,
    asset_id: Union[Unset, None, str] = UNSET,
) -> Response[ActivityStatisticsResponseDto]:
    """
    Args:
        album_id (str):
        asset_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityStatisticsResponseDto]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album_id: str,
    asset_id: Union[Unset, None, str] = UNSET,
) -> Optional[ActivityStatisticsResponseDto]:
    """
    Args:
        album_id (str):
        asset_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityStatisticsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            album_id=album_id,
            asset_id=asset_id,
        )
    ).parsed
