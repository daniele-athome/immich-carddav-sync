from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_command_dto import JobCommandDto
from ...models.job_name import JobName
from ...models.job_status_dto import JobStatusDto
from ...types import Response


def _get_kwargs(
    id: JobName,
    *,
    json_body: JobCommandDto,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/jobs/{id}".format(
            id=id,
        ),
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[JobStatusDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobStatusDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[JobStatusDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: JobName,
    *,
    client: AuthenticatedClient,
    json_body: JobCommandDto,
) -> Response[JobStatusDto]:
    """
    Args:
        id (JobName):
        json_body (JobCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobStatusDto]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: JobName,
    *,
    client: AuthenticatedClient,
    json_body: JobCommandDto,
) -> Optional[JobStatusDto]:
    """
    Args:
        id (JobName):
        json_body (JobCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobStatusDto
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: JobName,
    *,
    client: AuthenticatedClient,
    json_body: JobCommandDto,
) -> Response[JobStatusDto]:
    """
    Args:
        id (JobName):
        json_body (JobCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobStatusDto]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: JobName,
    *,
    client: AuthenticatedClient,
    json_body: JobCommandDto,
) -> Optional[JobStatusDto]:
    """
    Args:
        id (JobName):
        json_body (JobCommandDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobStatusDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
