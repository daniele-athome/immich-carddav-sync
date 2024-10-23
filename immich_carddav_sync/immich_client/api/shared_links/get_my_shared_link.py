from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shared_link_response_dto import SharedLinkResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["key"] = key

    params["password"] = password

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/shared-links/me",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SharedLinkResponseDto]:
    if response.status_code == 200:
        response_200 = SharedLinkResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SharedLinkResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    key: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
) -> Response[SharedLinkResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        password (Union[Unset, str]):  Example: password.
        token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        key=key,
        password=password,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    key: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
) -> Optional[SharedLinkResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        password (Union[Unset, str]):  Example: password.
        token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return sync_detailed(
        client=client,
        key=key,
        password=password,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
) -> Response[SharedLinkResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        password (Union[Unset, str]):  Example: password.
        token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        key=key,
        password=password,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    key: Union[Unset, str] = UNSET,
    password: Union[Unset, str] = UNSET,
    token: Union[Unset, str] = UNSET,
) -> Optional[SharedLinkResponseDto]:
    """
    Args:
        key (Union[Unset, str]):
        password (Union[Unset, str]):  Example: password.
        token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
            password=password,
            token=token,
        )
    ).parsed
