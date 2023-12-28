from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shared_link_response_dto import SharedLinkResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    password: Union[Unset, None, str] = UNSET,
    token: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["password"] = password

    params["token"] = token

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/shared-link/me",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SharedLinkResponseDto]:
    if response.status_code == HTTPStatus.OK:
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
    password: Union[Unset, None, str] = UNSET,
    token: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[SharedLinkResponseDto]:
    """
    Args:
        password (Union[Unset, None, str]):
        token (Union[Unset, None, str]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        password=password,
        token=token,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    password: Union[Unset, None, str] = UNSET,
    token: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[SharedLinkResponseDto]:
    """
    Args:
        password (Union[Unset, None, str]):
        token (Union[Unset, None, str]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return sync_detailed(
        client=client,
        password=password,
        token=token,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    password: Union[Unset, None, str] = UNSET,
    token: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Response[SharedLinkResponseDto]:
    """
    Args:
        password (Union[Unset, None, str]):
        token (Union[Unset, None, str]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharedLinkResponseDto]
    """

    kwargs = _get_kwargs(
        password=password,
        token=token,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    password: Union[Unset, None, str] = UNSET,
    token: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
) -> Optional[SharedLinkResponseDto]:
    """
    Args:
        password (Union[Unset, None, str]):
        token (Union[Unset, None, str]):
        key (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharedLinkResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            password=password,
            token=token,
            key=key,
        )
    ).parsed
