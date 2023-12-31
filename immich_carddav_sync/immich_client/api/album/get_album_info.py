from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_response_dto import AlbumResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    without_assets: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["withoutAssets"] = without_assets

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/album/{id}".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AlbumResponseDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AlbumResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AlbumResponseDto]:
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
    without_assets: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[AlbumResponseDto]:
    """
    Args:
        id (str):
        without_assets (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        without_assets=without_assets,
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
    without_assets: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[AlbumResponseDto]:
    """
    Args:
        id (str):
        without_assets (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponseDto
    """

    return sync_detailed(
        id=id,
        client=client,
        without_assets=without_assets,
        key=key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    without_assets: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[AlbumResponseDto]:
    """
    Args:
        id (str):
        without_assets (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        without_assets=without_assets,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    without_assets: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[AlbumResponseDto]:
    """
    Args:
        id (str):
        without_assets (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            without_assets=without_assets,
            key=key,
        )
    ).parsed
