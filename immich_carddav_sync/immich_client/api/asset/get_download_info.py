from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_info_dto import DownloadInfoDto
from ...models.download_response_dto import DownloadResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: DownloadInfoDto,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/asset/download/info",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DownloadResponseDto]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DownloadResponseDto.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DownloadResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DownloadInfoDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[DownloadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        json_body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadResponseDto]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: DownloadInfoDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[DownloadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        json_body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadResponseDto
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DownloadInfoDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[DownloadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        json_body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadResponseDto]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: DownloadInfoDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[DownloadResponseDto]:
    """
    Args:
        key (Union[Unset, None, str]):
        json_body (DownloadInfoDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            key=key,
        )
    ).parsed
