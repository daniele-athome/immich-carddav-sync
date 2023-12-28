import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_order import AssetOrder
from ...models.asset_response_dto import AssetResponseDto
from ...models.asset_type_enum import AssetTypeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, str] = UNSET,
    library_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AssetTypeEnum] = UNSET,
    order: Union[Unset, None, AssetOrder] = UNSET,
    device_asset_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    checksum: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_encoded: Union[Unset, None, bool] = UNSET,
    is_external: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_motion: Union[Unset, None, bool] = UNSET,
    is_offline: Union[Unset, None, bool] = UNSET,
    is_read_only: Union[Unset, None, bool] = UNSET,
    is_visible: Union[Unset, None, bool] = UNSET,
    with_deleted: Union[Unset, None, bool] = UNSET,
    with_stacked: Union[Unset, None, bool] = UNSET,
    with_exif: Union[Unset, None, bool] = UNSET,
    with_people: Union[Unset, None, bool] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_before: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_after: Union[Unset, None, datetime.datetime] = UNSET,
    taken_before: Union[Unset, None, datetime.datetime] = UNSET,
    taken_after: Union[Unset, None, datetime.datetime] = UNSET,
    original_file_name: Union[Unset, None, str] = UNSET,
    original_path: Union[Unset, None, str] = UNSET,
    resize_path: Union[Unset, None, str] = UNSET,
    webp_path: Union[Unset, None, str] = UNSET,
    encoded_video_path: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    lens_model: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, float] = UNSET,
    size: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["id"] = id

    params["libraryId"] = library_id

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["deviceAssetId"] = device_asset_id

    params["deviceId"] = device_id

    params["checksum"] = checksum

    params["isArchived"] = is_archived

    params["isEncoded"] = is_encoded

    params["isExternal"] = is_external

    params["isFavorite"] = is_favorite

    params["isMotion"] = is_motion

    params["isOffline"] = is_offline

    params["isReadOnly"] = is_read_only

    params["isVisible"] = is_visible

    params["withDeleted"] = with_deleted

    params["withStacked"] = with_stacked

    params["withExif"] = with_exif

    params["withPeople"] = with_people

    json_created_before: Union[Unset, None, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat() if created_before else None

    params["createdBefore"] = json_created_before

    json_created_after: Union[Unset, None, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat() if created_after else None

    params["createdAfter"] = json_created_after

    json_updated_before: Union[Unset, None, str] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat() if updated_before else None

    params["updatedBefore"] = json_updated_before

    json_updated_after: Union[Unset, None, str] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat() if updated_after else None

    params["updatedAfter"] = json_updated_after

    json_trashed_before: Union[Unset, None, str] = UNSET
    if not isinstance(trashed_before, Unset):
        json_trashed_before = trashed_before.isoformat() if trashed_before else None

    params["trashedBefore"] = json_trashed_before

    json_trashed_after: Union[Unset, None, str] = UNSET
    if not isinstance(trashed_after, Unset):
        json_trashed_after = trashed_after.isoformat() if trashed_after else None

    params["trashedAfter"] = json_trashed_after

    json_taken_before: Union[Unset, None, str] = UNSET
    if not isinstance(taken_before, Unset):
        json_taken_before = taken_before.isoformat() if taken_before else None

    params["takenBefore"] = json_taken_before

    json_taken_after: Union[Unset, None, str] = UNSET
    if not isinstance(taken_after, Unset):
        json_taken_after = taken_after.isoformat() if taken_after else None

    params["takenAfter"] = json_taken_after

    params["originalFileName"] = original_file_name

    params["originalPath"] = original_path

    params["resizePath"] = resize_path

    params["webpPath"] = webp_path

    params["encodedVideoPath"] = encoded_video_path

    params["city"] = city

    params["state"] = state

    params["country"] = country

    params["make"] = make

    params["model"] = model

    params["lensModel"] = lens_model

    params["page"] = page

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/assets",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AssetResponseDto"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssetResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AssetResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, str] = UNSET,
    library_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AssetTypeEnum] = UNSET,
    order: Union[Unset, None, AssetOrder] = UNSET,
    device_asset_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    checksum: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_encoded: Union[Unset, None, bool] = UNSET,
    is_external: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_motion: Union[Unset, None, bool] = UNSET,
    is_offline: Union[Unset, None, bool] = UNSET,
    is_read_only: Union[Unset, None, bool] = UNSET,
    is_visible: Union[Unset, None, bool] = UNSET,
    with_deleted: Union[Unset, None, bool] = UNSET,
    with_stacked: Union[Unset, None, bool] = UNSET,
    with_exif: Union[Unset, None, bool] = UNSET,
    with_people: Union[Unset, None, bool] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_before: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_after: Union[Unset, None, datetime.datetime] = UNSET,
    taken_before: Union[Unset, None, datetime.datetime] = UNSET,
    taken_after: Union[Unset, None, datetime.datetime] = UNSET,
    original_file_name: Union[Unset, None, str] = UNSET,
    original_path: Union[Unset, None, str] = UNSET,
    resize_path: Union[Unset, None, str] = UNSET,
    webp_path: Union[Unset, None, str] = UNSET,
    encoded_video_path: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    lens_model: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, float] = UNSET,
    size: Union[Unset, None, float] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """
    Args:
        id (Union[Unset, None, str]):
        library_id (Union[Unset, None, str]):
        type (Union[Unset, None, AssetTypeEnum]):
        order (Union[Unset, None, AssetOrder]):
        device_asset_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        checksum (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_encoded (Union[Unset, None, bool]):
        is_external (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        is_motion (Union[Unset, None, bool]):
        is_offline (Union[Unset, None, bool]):
        is_read_only (Union[Unset, None, bool]):
        is_visible (Union[Unset, None, bool]):
        with_deleted (Union[Unset, None, bool]):
        with_stacked (Union[Unset, None, bool]):
        with_exif (Union[Unset, None, bool]):
        with_people (Union[Unset, None, bool]):
        created_before (Union[Unset, None, datetime.datetime]):
        created_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        trashed_before (Union[Unset, None, datetime.datetime]):
        trashed_after (Union[Unset, None, datetime.datetime]):
        taken_before (Union[Unset, None, datetime.datetime]):
        taken_after (Union[Unset, None, datetime.datetime]):
        original_file_name (Union[Unset, None, str]):
        original_path (Union[Unset, None, str]):
        resize_path (Union[Unset, None, str]):
        webp_path (Union[Unset, None, str]):
        encoded_video_path (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        make (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        lens_model (Union[Unset, None, str]):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        id=id,
        library_id=library_id,
        type=type,
        order=order,
        device_asset_id=device_asset_id,
        device_id=device_id,
        checksum=checksum,
        is_archived=is_archived,
        is_encoded=is_encoded,
        is_external=is_external,
        is_favorite=is_favorite,
        is_motion=is_motion,
        is_offline=is_offline,
        is_read_only=is_read_only,
        is_visible=is_visible,
        with_deleted=with_deleted,
        with_stacked=with_stacked,
        with_exif=with_exif,
        with_people=with_people,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        trashed_before=trashed_before,
        trashed_after=trashed_after,
        taken_before=taken_before,
        taken_after=taken_after,
        original_file_name=original_file_name,
        original_path=original_path,
        resize_path=resize_path,
        webp_path=webp_path,
        encoded_video_path=encoded_video_path,
        city=city,
        state=state,
        country=country,
        make=make,
        model=model,
        lens_model=lens_model,
        page=page,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, str] = UNSET,
    library_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AssetTypeEnum] = UNSET,
    order: Union[Unset, None, AssetOrder] = UNSET,
    device_asset_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    checksum: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_encoded: Union[Unset, None, bool] = UNSET,
    is_external: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_motion: Union[Unset, None, bool] = UNSET,
    is_offline: Union[Unset, None, bool] = UNSET,
    is_read_only: Union[Unset, None, bool] = UNSET,
    is_visible: Union[Unset, None, bool] = UNSET,
    with_deleted: Union[Unset, None, bool] = UNSET,
    with_stacked: Union[Unset, None, bool] = UNSET,
    with_exif: Union[Unset, None, bool] = UNSET,
    with_people: Union[Unset, None, bool] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_before: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_after: Union[Unset, None, datetime.datetime] = UNSET,
    taken_before: Union[Unset, None, datetime.datetime] = UNSET,
    taken_after: Union[Unset, None, datetime.datetime] = UNSET,
    original_file_name: Union[Unset, None, str] = UNSET,
    original_path: Union[Unset, None, str] = UNSET,
    resize_path: Union[Unset, None, str] = UNSET,
    webp_path: Union[Unset, None, str] = UNSET,
    encoded_video_path: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    lens_model: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, float] = UNSET,
    size: Union[Unset, None, float] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """
    Args:
        id (Union[Unset, None, str]):
        library_id (Union[Unset, None, str]):
        type (Union[Unset, None, AssetTypeEnum]):
        order (Union[Unset, None, AssetOrder]):
        device_asset_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        checksum (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_encoded (Union[Unset, None, bool]):
        is_external (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        is_motion (Union[Unset, None, bool]):
        is_offline (Union[Unset, None, bool]):
        is_read_only (Union[Unset, None, bool]):
        is_visible (Union[Unset, None, bool]):
        with_deleted (Union[Unset, None, bool]):
        with_stacked (Union[Unset, None, bool]):
        with_exif (Union[Unset, None, bool]):
        with_people (Union[Unset, None, bool]):
        created_before (Union[Unset, None, datetime.datetime]):
        created_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        trashed_before (Union[Unset, None, datetime.datetime]):
        trashed_after (Union[Unset, None, datetime.datetime]):
        taken_before (Union[Unset, None, datetime.datetime]):
        taken_after (Union[Unset, None, datetime.datetime]):
        original_file_name (Union[Unset, None, str]):
        original_path (Union[Unset, None, str]):
        resize_path (Union[Unset, None, str]):
        webp_path (Union[Unset, None, str]):
        encoded_video_path (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        make (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        lens_model (Union[Unset, None, str]):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return sync_detailed(
        client=client,
        id=id,
        library_id=library_id,
        type=type,
        order=order,
        device_asset_id=device_asset_id,
        device_id=device_id,
        checksum=checksum,
        is_archived=is_archived,
        is_encoded=is_encoded,
        is_external=is_external,
        is_favorite=is_favorite,
        is_motion=is_motion,
        is_offline=is_offline,
        is_read_only=is_read_only,
        is_visible=is_visible,
        with_deleted=with_deleted,
        with_stacked=with_stacked,
        with_exif=with_exif,
        with_people=with_people,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        trashed_before=trashed_before,
        trashed_after=trashed_after,
        taken_before=taken_before,
        taken_after=taken_after,
        original_file_name=original_file_name,
        original_path=original_path,
        resize_path=resize_path,
        webp_path=webp_path,
        encoded_video_path=encoded_video_path,
        city=city,
        state=state,
        country=country,
        make=make,
        model=model,
        lens_model=lens_model,
        page=page,
        size=size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, str] = UNSET,
    library_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AssetTypeEnum] = UNSET,
    order: Union[Unset, None, AssetOrder] = UNSET,
    device_asset_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    checksum: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_encoded: Union[Unset, None, bool] = UNSET,
    is_external: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_motion: Union[Unset, None, bool] = UNSET,
    is_offline: Union[Unset, None, bool] = UNSET,
    is_read_only: Union[Unset, None, bool] = UNSET,
    is_visible: Union[Unset, None, bool] = UNSET,
    with_deleted: Union[Unset, None, bool] = UNSET,
    with_stacked: Union[Unset, None, bool] = UNSET,
    with_exif: Union[Unset, None, bool] = UNSET,
    with_people: Union[Unset, None, bool] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_before: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_after: Union[Unset, None, datetime.datetime] = UNSET,
    taken_before: Union[Unset, None, datetime.datetime] = UNSET,
    taken_after: Union[Unset, None, datetime.datetime] = UNSET,
    original_file_name: Union[Unset, None, str] = UNSET,
    original_path: Union[Unset, None, str] = UNSET,
    resize_path: Union[Unset, None, str] = UNSET,
    webp_path: Union[Unset, None, str] = UNSET,
    encoded_video_path: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    lens_model: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, float] = UNSET,
    size: Union[Unset, None, float] = UNSET,
) -> Response[List["AssetResponseDto"]]:
    """
    Args:
        id (Union[Unset, None, str]):
        library_id (Union[Unset, None, str]):
        type (Union[Unset, None, AssetTypeEnum]):
        order (Union[Unset, None, AssetOrder]):
        device_asset_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        checksum (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_encoded (Union[Unset, None, bool]):
        is_external (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        is_motion (Union[Unset, None, bool]):
        is_offline (Union[Unset, None, bool]):
        is_read_only (Union[Unset, None, bool]):
        is_visible (Union[Unset, None, bool]):
        with_deleted (Union[Unset, None, bool]):
        with_stacked (Union[Unset, None, bool]):
        with_exif (Union[Unset, None, bool]):
        with_people (Union[Unset, None, bool]):
        created_before (Union[Unset, None, datetime.datetime]):
        created_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        trashed_before (Union[Unset, None, datetime.datetime]):
        trashed_after (Union[Unset, None, datetime.datetime]):
        taken_before (Union[Unset, None, datetime.datetime]):
        taken_after (Union[Unset, None, datetime.datetime]):
        original_file_name (Union[Unset, None, str]):
        original_path (Union[Unset, None, str]):
        resize_path (Union[Unset, None, str]):
        webp_path (Union[Unset, None, str]):
        encoded_video_path (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        make (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        lens_model (Union[Unset, None, str]):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AssetResponseDto']]
    """

    kwargs = _get_kwargs(
        id=id,
        library_id=library_id,
        type=type,
        order=order,
        device_asset_id=device_asset_id,
        device_id=device_id,
        checksum=checksum,
        is_archived=is_archived,
        is_encoded=is_encoded,
        is_external=is_external,
        is_favorite=is_favorite,
        is_motion=is_motion,
        is_offline=is_offline,
        is_read_only=is_read_only,
        is_visible=is_visible,
        with_deleted=with_deleted,
        with_stacked=with_stacked,
        with_exif=with_exif,
        with_people=with_people,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        trashed_before=trashed_before,
        trashed_after=trashed_after,
        taken_before=taken_before,
        taken_after=taken_after,
        original_file_name=original_file_name,
        original_path=original_path,
        resize_path=resize_path,
        webp_path=webp_path,
        encoded_video_path=encoded_video_path,
        city=city,
        state=state,
        country=country,
        make=make,
        model=model,
        lens_model=lens_model,
        page=page,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, str] = UNSET,
    library_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AssetTypeEnum] = UNSET,
    order: Union[Unset, None, AssetOrder] = UNSET,
    device_asset_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    checksum: Union[Unset, None, str] = UNSET,
    is_archived: Union[Unset, None, bool] = UNSET,
    is_encoded: Union[Unset, None, bool] = UNSET,
    is_external: Union[Unset, None, bool] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_motion: Union[Unset, None, bool] = UNSET,
    is_offline: Union[Unset, None, bool] = UNSET,
    is_read_only: Union[Unset, None, bool] = UNSET,
    is_visible: Union[Unset, None, bool] = UNSET,
    with_deleted: Union[Unset, None, bool] = UNSET,
    with_stacked: Union[Unset, None, bool] = UNSET,
    with_exif: Union[Unset, None, bool] = UNSET,
    with_people: Union[Unset, None, bool] = UNSET,
    created_before: Union[Unset, None, datetime.datetime] = UNSET,
    created_after: Union[Unset, None, datetime.datetime] = UNSET,
    updated_before: Union[Unset, None, datetime.datetime] = UNSET,
    updated_after: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_before: Union[Unset, None, datetime.datetime] = UNSET,
    trashed_after: Union[Unset, None, datetime.datetime] = UNSET,
    taken_before: Union[Unset, None, datetime.datetime] = UNSET,
    taken_after: Union[Unset, None, datetime.datetime] = UNSET,
    original_file_name: Union[Unset, None, str] = UNSET,
    original_path: Union[Unset, None, str] = UNSET,
    resize_path: Union[Unset, None, str] = UNSET,
    webp_path: Union[Unset, None, str] = UNSET,
    encoded_video_path: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
    country: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    lens_model: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, float] = UNSET,
    size: Union[Unset, None, float] = UNSET,
) -> Optional[List["AssetResponseDto"]]:
    """
    Args:
        id (Union[Unset, None, str]):
        library_id (Union[Unset, None, str]):
        type (Union[Unset, None, AssetTypeEnum]):
        order (Union[Unset, None, AssetOrder]):
        device_asset_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        checksum (Union[Unset, None, str]):
        is_archived (Union[Unset, None, bool]):
        is_encoded (Union[Unset, None, bool]):
        is_external (Union[Unset, None, bool]):
        is_favorite (Union[Unset, None, bool]):
        is_motion (Union[Unset, None, bool]):
        is_offline (Union[Unset, None, bool]):
        is_read_only (Union[Unset, None, bool]):
        is_visible (Union[Unset, None, bool]):
        with_deleted (Union[Unset, None, bool]):
        with_stacked (Union[Unset, None, bool]):
        with_exif (Union[Unset, None, bool]):
        with_people (Union[Unset, None, bool]):
        created_before (Union[Unset, None, datetime.datetime]):
        created_after (Union[Unset, None, datetime.datetime]):
        updated_before (Union[Unset, None, datetime.datetime]):
        updated_after (Union[Unset, None, datetime.datetime]):
        trashed_before (Union[Unset, None, datetime.datetime]):
        trashed_after (Union[Unset, None, datetime.datetime]):
        taken_before (Union[Unset, None, datetime.datetime]):
        taken_after (Union[Unset, None, datetime.datetime]):
        original_file_name (Union[Unset, None, str]):
        original_path (Union[Unset, None, str]):
        resize_path (Union[Unset, None, str]):
        webp_path (Union[Unset, None, str]):
        encoded_video_path (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        make (Union[Unset, None, str]):
        model (Union[Unset, None, str]):
        lens_model (Union[Unset, None, str]):
        page (Union[Unset, None, float]):
        size (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AssetResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            library_id=library_id,
            type=type,
            order=order,
            device_asset_id=device_asset_id,
            device_id=device_id,
            checksum=checksum,
            is_archived=is_archived,
            is_encoded=is_encoded,
            is_external=is_external,
            is_favorite=is_favorite,
            is_motion=is_motion,
            is_offline=is_offline,
            is_read_only=is_read_only,
            is_visible=is_visible,
            with_deleted=with_deleted,
            with_stacked=with_stacked,
            with_exif=with_exif,
            with_people=with_people,
            created_before=created_before,
            created_after=created_after,
            updated_before=updated_before,
            updated_after=updated_after,
            trashed_before=trashed_before,
            trashed_after=trashed_after,
            taken_before=taken_before,
            taken_after=taken_after,
            original_file_name=original_file_name,
            original_path=original_path,
            resize_path=resize_path,
            webp_path=webp_path,
            encoded_video_path=encoded_video_path,
            city=city,
            state=state,
            country=country,
            make=make,
            model=model,
            lens_model=lens_model,
            page=page,
            size=size,
        )
    ).parsed
