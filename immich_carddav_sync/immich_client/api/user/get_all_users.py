from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_response_dto import UserResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    is_all: bool,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["isAll"] = is_all

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/user",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["UserResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["UserResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_all: bool,
) -> Response[List["UserResponseDto"]]:
    """
    Args:
        is_all (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserResponseDto']]
    """

    kwargs = _get_kwargs(
        is_all=is_all,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_all: bool,
) -> Optional[List["UserResponseDto"]]:
    """
    Args:
        is_all (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserResponseDto']
    """

    return sync_detailed(
        client=client,
        is_all=is_all,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_all: bool,
) -> Response[List["UserResponseDto"]]:
    """
    Args:
        is_all (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserResponseDto']]
    """

    kwargs = _get_kwargs(
        is_all=is_all,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_all: bool,
) -> Optional[List["UserResponseDto"]]:
    """
    Args:
        is_all (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            is_all=is_all,
        )
    ).parsed
