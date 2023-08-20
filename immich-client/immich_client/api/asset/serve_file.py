from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: str,
    *,
    is_thumb: Union[Unset, None, bool] = UNSET,
    is_web: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["isThumb"] = is_thumb

    params["isWeb"] = is_web

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/asset/file/{id}".format(
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
    is_thumb: Union[Unset, None, bool] = UNSET,
    is_web: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        id (str):
        is_thumb (Union[Unset, None, bool]):
        is_web (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        is_thumb=is_thumb,
        is_web=is_web,
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
    is_thumb: Union[Unset, None, bool] = UNSET,
    is_web: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        id (str):
        is_thumb (Union[Unset, None, bool]):
        is_web (Union[Unset, None, bool]):
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
        is_thumb=is_thumb,
        is_web=is_web,
        key=key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    is_thumb: Union[Unset, None, bool] = UNSET,
    is_web: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[File]:
    """
    Args:
        id (str):
        is_thumb (Union[Unset, None, bool]):
        is_web (Union[Unset, None, bool]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        id=id,
        is_thumb=is_thumb,
        is_web=is_web,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    is_thumb: Union[Unset, None, bool] = UNSET,
    is_web: Union[Unset, None, bool] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[File]:
    """
    Args:
        id (str):
        is_thumb (Union[Unset, None, bool]):
        is_web (Union[Unset, None, bool]):
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
            is_thumb=is_thumb,
            is_web=is_web,
            key=key,
        )
    ).parsed
