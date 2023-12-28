from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.person_response_dto import PersonResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str,
    with_hidden: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["name"] = name

    params["withHidden"] = with_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/search/person",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["PersonResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PersonResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["PersonResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    with_hidden: Union[Unset, None, bool] = UNSET,
) -> Response[List["PersonResponseDto"]]:
    """
    Args:
        name (str):
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PersonResponseDto']]
    """

    kwargs = _get_kwargs(
        name=name,
        with_hidden=with_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: str,
    with_hidden: Union[Unset, None, bool] = UNSET,
) -> Optional[List["PersonResponseDto"]]:
    """
    Args:
        name (str):
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PersonResponseDto']
    """

    return sync_detailed(
        client=client,
        name=name,
        with_hidden=with_hidden,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    with_hidden: Union[Unset, None, bool] = UNSET,
) -> Response[List["PersonResponseDto"]]:
    """
    Args:
        name (str):
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PersonResponseDto']]
    """

    kwargs = _get_kwargs(
        name=name,
        with_hidden=with_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str,
    with_hidden: Union[Unset, None, bool] = UNSET,
) -> Optional[List["PersonResponseDto"]]:
    """
    Args:
        name (str):
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PersonResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            with_hidden=with_hidden,
        )
    ).parsed
