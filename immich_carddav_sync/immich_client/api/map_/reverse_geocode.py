from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.map_reverse_geocode_response_dto import MapReverseGeocodeResponseDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    lat: float,
    lon: float,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["lat"] = lat

    params["lon"] = lon

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/map/reverse-geocode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["MapReverseGeocodeResponseDto"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MapReverseGeocodeResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["MapReverseGeocodeResponseDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
) -> Response[List["MapReverseGeocodeResponseDto"]]:
    """
    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapReverseGeocodeResponseDto']]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
) -> Optional[List["MapReverseGeocodeResponseDto"]]:
    """
    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapReverseGeocodeResponseDto']
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lon=lon,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
) -> Response[List["MapReverseGeocodeResponseDto"]]:
    """
    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MapReverseGeocodeResponseDto']]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
) -> Optional[List["MapReverseGeocodeResponseDto"]]:
    """
    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MapReverseGeocodeResponseDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lon=lon,
        )
    ).parsed
