from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_profile_image_dto import CreateProfileImageDto
from ...models.create_profile_image_response_dto import CreateProfileImageResponseDto
from ...types import Response


def _get_kwargs(
    *,
    multipart_data: CreateProfileImageDto,
) -> Dict[str, Any]:
    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/user/profile-image",
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateProfileImageResponseDto]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateProfileImageResponseDto.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateProfileImageResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateProfileImageDto,
) -> Response[CreateProfileImageResponseDto]:
    """
    Args:
        multipart_data (CreateProfileImageDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProfileImageResponseDto]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateProfileImageDto,
) -> Optional[CreateProfileImageResponseDto]:
    """
    Args:
        multipart_data (CreateProfileImageDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProfileImageResponseDto
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateProfileImageDto,
) -> Response[CreateProfileImageResponseDto]:
    """
    Args:
        multipart_data (CreateProfileImageDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProfileImageResponseDto]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateProfileImageDto,
) -> Optional[CreateProfileImageResponseDto]:
    """
    Args:
        multipart_data (CreateProfileImageDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProfileImageResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
