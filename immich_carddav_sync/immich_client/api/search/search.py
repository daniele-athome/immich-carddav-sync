from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_response_dto import SearchResponseDto
from ...models.search_type import SearchType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    clip: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, SearchType] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["q"] = q

    params["query"] = query

    params["clip"] = clip

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["recent"] = recent

    params["motion"] = motion

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/search",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SearchResponseDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResponseDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SearchResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    clip: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, SearchType] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Response[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        recent (Union[Unset, None, bool]):
        motion (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponseDto]
    """

    kwargs = _get_kwargs(
        q=q,
        query=query,
        clip=clip,
        type=type,
        recent=recent,
        motion=motion,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    clip: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, SearchType] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Optional[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        recent (Union[Unset, None, bool]):
        motion (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponseDto
    """

    return sync_detailed(
        client=client,
        q=q,
        query=query,
        clip=clip,
        type=type,
        recent=recent,
        motion=motion,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    clip: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, SearchType] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Response[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        recent (Union[Unset, None, bool]):
        motion (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponseDto]
    """

    kwargs = _get_kwargs(
        q=q,
        query=query,
        clip=clip,
        type=type,
        recent=recent,
        motion=motion,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    clip: Union[Unset, None, bool] = UNSET,
    type: Union[Unset, None, SearchType] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Optional[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        recent (Union[Unset, None, bool]):
        motion (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            query=query,
            clip=clip,
            type=type,
            recent=recent,
            motion=motion,
        )
    ).parsed
