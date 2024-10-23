from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_suggestion_type import SearchSuggestionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: Union[Unset, str] = UNSET,
    include_null: Union[Unset, bool] = UNSET,
    make: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    type: SearchSuggestionType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["country"] = country

    params["includeNull"] = include_null

    params["make"] = make

    params["model"] = model

    params["state"] = state

    json_type = type.value
    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/search/suggestions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List[str]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = UNSET,
    include_null: Union[Unset, bool] = UNSET,
    make: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    type: SearchSuggestionType,
) -> Response[List[str]]:
    """
    Args:
        country (Union[Unset, str]):
        include_null (Union[Unset, bool]):
        make (Union[Unset, str]):
        model (Union[Unset, str]):
        state (Union[Unset, str]):
        type (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        country=country,
        include_null=include_null,
        make=make,
        model=model,
        state=state,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = UNSET,
    include_null: Union[Unset, bool] = UNSET,
    make: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    type: SearchSuggestionType,
) -> Optional[List[str]]:
    """
    Args:
        country (Union[Unset, str]):
        include_null (Union[Unset, bool]):
        make (Union[Unset, str]):
        model (Union[Unset, str]):
        state (Union[Unset, str]):
        type (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return sync_detailed(
        client=client,
        country=country,
        include_null=include_null,
        make=make,
        model=model,
        state=state,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = UNSET,
    include_null: Union[Unset, bool] = UNSET,
    make: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    type: SearchSuggestionType,
) -> Response[List[str]]:
    """
    Args:
        country (Union[Unset, str]):
        include_null (Union[Unset, bool]):
        make (Union[Unset, str]):
        model (Union[Unset, str]):
        state (Union[Unset, str]):
        type (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        country=country,
        include_null=include_null,
        make=make,
        model=model,
        state=state,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = UNSET,
    include_null: Union[Unset, bool] = UNSET,
    make: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    type: SearchSuggestionType,
) -> Optional[List[str]]:
    """
    Args:
        country (Union[Unset, str]):
        include_null (Union[Unset, bool]):
        make (Union[Unset, str]):
        model (Union[Unset, str]):
        state (Union[Unset, str]):
        type (SearchSuggestionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            include_null=include_null,
            make=make,
            model=model,
            state=state,
            type=type,
        )
    ).parsed
