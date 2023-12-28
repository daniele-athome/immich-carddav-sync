from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_file_upload_response_dto import AssetFileUploadResponseDto
from ...models.create_asset_dto import CreateAssetDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    multipart_data: CreateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/asset/upload",
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetFileUploadResponseDto]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AssetFileUploadResponseDto.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetFileUploadResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[AssetFileUploadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        multipart_data (CreateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetFileUploadResponseDto]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[AssetFileUploadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        multipart_data (CreateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetFileUploadResponseDto
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[AssetFileUploadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        multipart_data (CreateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetFileUploadResponseDto]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[AssetFileUploadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        multipart_data (CreateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetFileUploadResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            key=key,
        )
    ).parsed
