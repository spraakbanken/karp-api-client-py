from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_error_schema import UserErrorSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    resources: None | str,
    compile_: None | str,
    columns: str | Unset = "resourceId=_count",
    sort: str | Unset = "asc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_resources: None | str
    json_resources = resources
    params["resources"] = json_resources

    json_compile_: None | str
    json_compile_ = compile_
    params["compile"] = json_compile_

    params["columns"] = columns

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | UserErrorSchema | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = UserErrorSchema.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | UserErrorSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    resources: None | str,
    compile_: None | str,
    columns: str | Unset = "resourceId=_count",
    sort: str | Unset = "asc",
) -> Response[Any | HTTPValidationError | UserErrorSchema]:
    """Count

     From each provided resource, get the entries that match the query q. See
    http://ws.spraakbanken.gu.se/ws/karp/v7 for a description of the query language.

    Compile the matching entries on the fields in compile.

    Add additional data requested by using the `columns` parameter.

    ### Sorting

    Sorting is supported for fields that are used in `compile`. The default fields are all the fields in
    `compile`
    (**ascending** order) (they themselves sorted alphabetically, just like the columns).

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        compile_ (None | str):
            A list of fields to compile statistics on, for example `baseform`, `pos`,
            `normalized_form`
        columns (str | Unset):
            Add extra data columns to the result. For example: `field1=val_field1,field2=val_field2`

            The left-hand side of `=` denotes  a field that will be used to create columns. Good
            examples
            are `resourceId` and `ud_pos`. For each unique value in the result, a column will be
            created
            and the field in the right-hand side of `=`
            will be used for values in the cells of that column. If there are multiple values for the
            right-hand side field they
            will be shown as a list.

            It is possible to replace the field of the right-hand side with the keyword `_count` -
            `columns=resourceId=_count`.
            This is the default value if `columns` is omitted. With this, the number of
            hits per unique value of the selected field will be shown.

            The total number of rows and columns from `compile` will always be shown regardless of the
            value of `columns`.
             Default: 'resourceId=_count'.
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserErrorSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        resources=resources,
        compile_=compile_,
        columns=columns,
        sort=sort,
    )

    response = client.get_sync_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    resources: None | str,
    compile_: None | str,
    columns: str | Unset = "resourceId=_count",
    sort: str | Unset = "asc",
) -> Any | HTTPValidationError | UserErrorSchema | None:
    """Count

     From each provided resource, get the entries that match the query q. See
    http://ws.spraakbanken.gu.se/ws/karp/v7 for a description of the query language.

    Compile the matching entries on the fields in compile.

    Add additional data requested by using the `columns` parameter.

    ### Sorting

    Sorting is supported for fields that are used in `compile`. The default fields are all the fields in
    `compile`
    (**ascending** order) (they themselves sorted alphabetically, just like the columns).

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        compile_ (None | str):
            A list of fields to compile statistics on, for example `baseform`, `pos`,
            `normalized_form`
        columns (str | Unset):
            Add extra data columns to the result. For example: `field1=val_field1,field2=val_field2`

            The left-hand side of `=` denotes  a field that will be used to create columns. Good
            examples
            are `resourceId` and `ud_pos`. For each unique value in the result, a column will be
            created
            and the field in the right-hand side of `=`
            will be used for values in the cells of that column. If there are multiple values for the
            right-hand side field they
            will be shown as a list.

            It is possible to replace the field of the right-hand side with the keyword `_count` -
            `columns=resourceId=_count`.
            This is the default value if `columns` is omitted. With this, the number of
            hits per unique value of the selected field will be shown.

            The total number of rows and columns from `compile` will always be shown regardless of the
            value of `columns`.
             Default: 'resourceId=_count'.
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserErrorSchema
    """

    return sync_detailed(
        client=client,
        q=q,
        resources=resources,
        compile_=compile_,
        columns=columns,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    resources: None | str,
    compile_: None | str,
    columns: str | Unset = "resourceId=_count",
    sort: str | Unset = "asc",
) -> Response[Any | HTTPValidationError | UserErrorSchema]:
    """Count

     From each provided resource, get the entries that match the query q. See
    http://ws.spraakbanken.gu.se/ws/karp/v7 for a description of the query language.

    Compile the matching entries on the fields in compile.

    Add additional data requested by using the `columns` parameter.

    ### Sorting

    Sorting is supported for fields that are used in `compile`. The default fields are all the fields in
    `compile`
    (**ascending** order) (they themselves sorted alphabetically, just like the columns).

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        compile_ (None | str):
            A list of fields to compile statistics on, for example `baseform`, `pos`,
            `normalized_form`
        columns (str | Unset):
            Add extra data columns to the result. For example: `field1=val_field1,field2=val_field2`

            The left-hand side of `=` denotes  a field that will be used to create columns. Good
            examples
            are `resourceId` and `ud_pos`. For each unique value in the result, a column will be
            created
            and the field in the right-hand side of `=`
            will be used for values in the cells of that column. If there are multiple values for the
            right-hand side field they
            will be shown as a list.

            It is possible to replace the field of the right-hand side with the keyword `_count` -
            `columns=resourceId=_count`.
            This is the default value if `columns` is omitted. With this, the number of
            hits per unique value of the selected field will be shown.

            The total number of rows and columns from `compile` will always be shown regardless of the
            value of `columns`.
             Default: 'resourceId=_count'.
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | UserErrorSchema]
    """

    kwargs = _get_kwargs(
        q=q,
        resources=resources,
        compile_=compile_,
        columns=columns,
        sort=sort,
    )

    response = await client.get_async_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: None | str | Unset = UNSET,
    resources: None | str,
    compile_: None | str,
    columns: str | Unset = "resourceId=_count",
    sort: str | Unset = "asc",
) -> Any | HTTPValidationError | UserErrorSchema | None:
    """Count

     From each provided resource, get the entries that match the query q. See
    http://ws.spraakbanken.gu.se/ws/karp/v7 for a description of the query language.

    Compile the matching entries on the fields in compile.

    Add additional data requested by using the `columns` parameter.

    ### Sorting

    Sorting is supported for fields that are used in `compile`. The default fields are all the fields in
    `compile`
    (**ascending** order) (they themselves sorted alphabetically, just like the columns).

    Args:
        q (None | str | Unset): The query. See https://ws.spraakbanken.gu.se/docs/karp for a
            description of the query language, however, Karp-s does not support sub-queries, exists,
            missing and freetext.
        resources (None | str):
            A comma-separated list of resource ID:s, for example `saldo`
        compile_ (None | str):
            A list of fields to compile statistics on, for example `baseform`, `pos`,
            `normalized_form`
        columns (str | Unset):
            Add extra data columns to the result. For example: `field1=val_field1,field2=val_field2`

            The left-hand side of `=` denotes  a field that will be used to create columns. Good
            examples
            are `resourceId` and `ud_pos`. For each unique value in the result, a column will be
            created
            and the field in the right-hand side of `=`
            will be used for values in the cells of that column. If there are multiple values for the
            right-hand side field they
            will be shown as a list.

            It is possible to replace the field of the right-hand side with the keyword `_count` -
            `columns=resourceId=_count`.
            This is the default value if `columns` is omitted. With this, the number of
            hits per unique value of the selected field will be shown.

            The total number of rows and columns from `compile` will always be shown regardless of the
            value of `columns`.
             Default: 'resourceId=_count'.
        sort (str | Unset):
            See [Sorting the results](#section/Sorting-the-results) and API call description for more
            information.
             Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | UserErrorSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            resources=resources,
            compile_=compile_,
            columns=columns,
            sort=sort,
        )
    ).parsed
