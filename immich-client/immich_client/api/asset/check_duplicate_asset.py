from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_duplicate_asset_dto import CheckDuplicateAssetDto
from ...models.check_duplicate_asset_response_dto import CheckDuplicateAssetResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CheckDuplicateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/asset/check",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CheckDuplicateAssetResponseDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CheckDuplicateAssetResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CheckDuplicateAssetResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CheckDuplicateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[CheckDuplicateAssetResponseDto]:
    """Check duplicated asset before uploading - for Web upload used

    Args:
        key (Union[Unset, None, str]):
        json_body (CheckDuplicateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckDuplicateAssetResponseDto]
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
    json_body: CheckDuplicateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[CheckDuplicateAssetResponseDto]:
    """Check duplicated asset before uploading - for Web upload used

    Args:
        key (Union[Unset, None, str]):
        json_body (CheckDuplicateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckDuplicateAssetResponseDto
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CheckDuplicateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Response[CheckDuplicateAssetResponseDto]:
    """Check duplicated asset before uploading - for Web upload used

    Args:
        key (Union[Unset, None, str]):
        json_body (CheckDuplicateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckDuplicateAssetResponseDto]
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
    json_body: CheckDuplicateAssetDto,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[CheckDuplicateAssetResponseDto]:
    """Check duplicated asset before uploading - for Web upload used

    Args:
        key (Union[Unset, None, str]):
        json_body (CheckDuplicateAssetDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckDuplicateAssetResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            key=key,
        )
    ).parsed
