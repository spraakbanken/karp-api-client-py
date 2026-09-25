"""Karp API client command-line."""

import datetime
import sys
import typing as t

import json_arrays
import typer
from returns.result import Failure, Success

from karp_api_client import RedClient
from karp_api_client.api.red import querying

app = typer.Typer(help="Karp Red API client")


@app.command()
def query(
    resources: list[str],
    output: t.Annotated[str | None, typer.Option(help="Output to this path")] = None,
    size: t.Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Query the given resources."""
    if output is None:
        output = f"karp-query-{datetime.datetime.now()}.jsonl"
        print(f"Output will be written to '{output}'", file=sys.stderr)  # noqa: T201
    client = RedClient()
    response = querying.query_sync(",".join(resources), client=client, query_options=querying.QueryOptions(size=size))

    match response:
        case Success(resp):
            if resp.parsed is None:
                print("No response", file=sys.stderr)  # noqa: T201
                return
            json_arrays.dump_to_file((hit.to_dict() for hit in resp.parsed.hits), output)
        case Failure(err):
            print(f"Error occurred!\n{err}", file=sys.stderr)  # noqa: T201
            sys.exit(2)
