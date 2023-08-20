from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

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
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    exif_info_city: Union[Unset, None, str] = UNSET,
    exif_info_state: Union[Unset, None, str] = UNSET,
    exif_info_country: Union[Unset, None, str] = UNSET,
    exif_info_make: Union[Unset, None, str] = UNSET,
    exif_info_model: Union[Unset, None, str] = UNSET,
    exif_info_projection_type: Union[Unset, None, str] = UNSET,
    smart_info_objects: Union[Unset, None, List[str]] = UNSET,
    smart_info_tags: Union[Unset, None, List[str]] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["q"] = q

    params["query"] = query

    params["clip"] = clip

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["isFavorite"] = is_favorite

    params["isArchived"] = is_archived

    params["exifInfo.city"] = exif_info_city

    params["exifInfo.state"] = exif_info_state

    params["exifInfo.country"] = exif_info_country

    params["exifInfo.make"] = exif_info_make

    params["exifInfo.model"] = exif_info_model

    params["exifInfo.projectionType"] = exif_info_projection_type

    json_smart_info_objects: Union[Unset, None, List[str]] = UNSET
    if not isinstance(smart_info_objects, Unset):
        if smart_info_objects is None:
            json_smart_info_objects = None
        else:
            json_smart_info_objects = smart_info_objects

    params["smartInfo.objects"] = json_smart_info_objects

    json_smart_info_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(smart_info_tags, Unset):
        if smart_info_tags is None:
            json_smart_info_tags = None
        else:
            json_smart_info_tags = smart_info_tags

    params["smartInfo.tags"] = json_smart_info_tags

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
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    exif_info_city: Union[Unset, None, str] = UNSET,
    exif_info_state: Union[Unset, None, str] = UNSET,
    exif_info_country: Union[Unset, None, str] = UNSET,
    exif_info_make: Union[Unset, None, str] = UNSET,
    exif_info_model: Union[Unset, None, str] = UNSET,
    exif_info_projection_type: Union[Unset, None, str] = UNSET,
    smart_info_objects: Union[Unset, None, List[str]] = UNSET,
    smart_info_tags: Union[Unset, None, List[str]] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Response[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        exif_info_city (Union[Unset, None, str]):
        exif_info_state (Union[Unset, None, str]):
        exif_info_country (Union[Unset, None, str]):
        exif_info_make (Union[Unset, None, str]):
        exif_info_model (Union[Unset, None, str]):
        exif_info_projection_type (Union[Unset, None, str]):
        smart_info_objects (Union[Unset, None, List[str]]):
        smart_info_tags (Union[Unset, None, List[str]]):
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
        is_favorite=is_favorite,
        is_archived=is_archived,
        exif_info_city=exif_info_city,
        exif_info_state=exif_info_state,
        exif_info_country=exif_info_country,
        exif_info_make=exif_info_make,
        exif_info_model=exif_info_model,
        exif_info_projection_type=exif_info_projection_type,
        smart_info_objects=smart_info_objects,
        smart_info_tags=smart_info_tags,
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
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    exif_info_city: Union[Unset, None, str] = UNSET,
    exif_info_state: Union[Unset, None, str] = UNSET,
    exif_info_country: Union[Unset, None, str] = UNSET,
    exif_info_make: Union[Unset, None, str] = UNSET,
    exif_info_model: Union[Unset, None, str] = UNSET,
    exif_info_projection_type: Union[Unset, None, str] = UNSET,
    smart_info_objects: Union[Unset, None, List[str]] = UNSET,
    smart_info_tags: Union[Unset, None, List[str]] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Optional[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        exif_info_city (Union[Unset, None, str]):
        exif_info_state (Union[Unset, None, str]):
        exif_info_country (Union[Unset, None, str]):
        exif_info_make (Union[Unset, None, str]):
        exif_info_model (Union[Unset, None, str]):
        exif_info_projection_type (Union[Unset, None, str]):
        smart_info_objects (Union[Unset, None, List[str]]):
        smart_info_tags (Union[Unset, None, List[str]]):
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
        is_favorite=is_favorite,
        is_archived=is_archived,
        exif_info_city=exif_info_city,
        exif_info_state=exif_info_state,
        exif_info_country=exif_info_country,
        exif_info_make=exif_info_make,
        exif_info_model=exif_info_model,
        exif_info_projection_type=exif_info_projection_type,
        smart_info_objects=smart_info_objects,
        smart_info_tags=smart_info_tags,
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
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    exif_info_city: Union[Unset, None, str] = UNSET,
    exif_info_state: Union[Unset, None, str] = UNSET,
    exif_info_country: Union[Unset, None, str] = UNSET,
    exif_info_make: Union[Unset, None, str] = UNSET,
    exif_info_model: Union[Unset, None, str] = UNSET,
    exif_info_projection_type: Union[Unset, None, str] = UNSET,
    smart_info_objects: Union[Unset, None, List[str]] = UNSET,
    smart_info_tags: Union[Unset, None, List[str]] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Response[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        exif_info_city (Union[Unset, None, str]):
        exif_info_state (Union[Unset, None, str]):
        exif_info_country (Union[Unset, None, str]):
        exif_info_make (Union[Unset, None, str]):
        exif_info_model (Union[Unset, None, str]):
        exif_info_projection_type (Union[Unset, None, str]):
        smart_info_objects (Union[Unset, None, List[str]]):
        smart_info_tags (Union[Unset, None, List[str]]):
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
        is_favorite=is_favorite,
        is_archived=is_archived,
        exif_info_city=exif_info_city,
        exif_info_state=exif_info_state,
        exif_info_country=exif_info_country,
        exif_info_make=exif_info_make,
        exif_info_model=exif_info_model,
        exif_info_projection_type=exif_info_projection_type,
        smart_info_objects=smart_info_objects,
        smart_info_tags=smart_info_tags,
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
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    exif_info_city: Union[Unset, None, str] = UNSET,
    exif_info_state: Union[Unset, None, str] = UNSET,
    exif_info_country: Union[Unset, None, str] = UNSET,
    exif_info_make: Union[Unset, None, str] = UNSET,
    exif_info_model: Union[Unset, None, str] = UNSET,
    exif_info_projection_type: Union[Unset, None, str] = UNSET,
    smart_info_objects: Union[Unset, None, List[str]] = UNSET,
    smart_info_tags: Union[Unset, None, List[str]] = UNSET,
    recent: Union[Unset, None, bool] = UNSET,
    motion: Union[Unset, None, bool] = UNSET,
) -> Optional[SearchResponseDto]:
    """
    Args:
        q (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        clip (Union[Unset, None, bool]):
        type (Union[Unset, None, SearchType]):
        is_favorite (Union[Unset, None, bool]):
        is_archived (Union[Unset, None, bool]):
        exif_info_city (Union[Unset, None, str]):
        exif_info_state (Union[Unset, None, str]):
        exif_info_country (Union[Unset, None, str]):
        exif_info_make (Union[Unset, None, str]):
        exif_info_model (Union[Unset, None, str]):
        exif_info_projection_type (Union[Unset, None, str]):
        smart_info_objects (Union[Unset, None, List[str]]):
        smart_info_tags (Union[Unset, None, List[str]]):
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
            is_favorite=is_favorite,
            is_archived=is_archived,
            exif_info_city=exif_info_city,
            exif_info_state=exif_info_state,
            exif_info_country=exif_info_country,
            exif_info_make=exif_info_make,
            exif_info_model=exif_info_model,
            exif_info_projection_type=exif_info_projection_type,
            smart_info_objects=smart_info_objects,
            smart_info_tags=smart_info_tags,
            recent=recent,
            motion=motion,
        )
    ).parsed
