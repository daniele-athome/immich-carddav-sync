from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.thumbnail_format import ThumbnailFormat
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: str,
    *,
    format_: Union[Unset, None, ThumbnailFormat] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset/thumbnail/{id}".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[File]:
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
    format_: Union[Unset, None, ThumbnailFormat] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ThumbnailFormat]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
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
    format_: Union[Unset, None, ThumbnailFormat] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ThumbnailFormat]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
        key=key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, ThumbnailFormat] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ThumbnailFormat]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, ThumbnailFormat] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ThumbnailFormat]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
            key=key,
        )
    ).parsed
