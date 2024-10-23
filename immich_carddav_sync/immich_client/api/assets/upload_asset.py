from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_media_create_dto import AssetMediaCreateDto
from ...models.asset_media_response_dto import AssetMediaResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AssetMediaCreateDto,
    key: Union[Unset, str] = UNSET,
    x_immich_checksum: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_immich_checksum, Unset):
        headers["x-immich-checksum"] = x_immich_checksum

    params: Dict[str, Any] = {}

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/assets",
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetMediaResponseDto]:
    if response.status_code == 201:
        response_201 = AssetMediaResponseDto.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetMediaResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetMediaCreateDto,
    key: Union[Unset, str] = UNSET,
    x_immich_checksum: Union[Unset, str] = UNSET,
) -> Response[AssetMediaResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        x_immich_checksum (Union[Unset, str]):
        body (AssetMediaCreateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetMediaResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        key=key,
        x_immich_checksum=x_immich_checksum,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AssetMediaCreateDto,
    key: Union[Unset, str] = UNSET,
    x_immich_checksum: Union[Unset, str] = UNSET,
) -> Optional[AssetMediaResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        x_immich_checksum (Union[Unset, str]):
        body (AssetMediaCreateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetMediaResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        key=key,
        x_immich_checksum=x_immich_checksum,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetMediaCreateDto,
    key: Union[Unset, str] = UNSET,
    x_immich_checksum: Union[Unset, str] = UNSET,
) -> Response[AssetMediaResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        x_immich_checksum (Union[Unset, str]):
        body (AssetMediaCreateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetMediaResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        key=key,
        x_immich_checksum=x_immich_checksum,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AssetMediaCreateDto,
    key: Union[Unset, str] = UNSET,
    x_immich_checksum: Union[Unset, str] = UNSET,
) -> Optional[AssetMediaResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        x_immich_checksum (Union[Unset, str]):
        body (AssetMediaCreateDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetMediaResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            key=key,
            x_immich_checksum=x_immich_checksum,
        )
    ).parsed
