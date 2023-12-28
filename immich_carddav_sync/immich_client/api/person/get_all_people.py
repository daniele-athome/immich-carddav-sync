from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.people_response_dto import PeopleResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_hidden: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["withHidden"] = with_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/person",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PeopleResponseDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PeopleResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PeopleResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    with_hidden: Union[Unset, None, bool] = False,
) -> Response[PeopleResponseDto]:
    """
    Args:
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PeopleResponseDto]
    """

    kwargs = _get_kwargs(
        with_hidden=with_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    with_hidden: Union[Unset, None, bool] = False,
) -> Optional[PeopleResponseDto]:
    """
    Args:
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PeopleResponseDto
    """

    return sync_detailed(
        client=client,
        with_hidden=with_hidden,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    with_hidden: Union[Unset, None, bool] = False,
) -> Response[PeopleResponseDto]:
    """
    Args:
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PeopleResponseDto]
    """

    kwargs = _get_kwargs(
        with_hidden=with_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    with_hidden: Union[Unset, None, bool] = False,
) -> Optional[PeopleResponseDto]:
    """
    Args:
        with_hidden (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PeopleResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            with_hidden=with_hidden,
        )
    ).parsed
