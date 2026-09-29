"""Karp API client command-line."""

import sys
import typing as t
from pathlib import Path

import json_arrays
import typer
from karp_red_api_client import RedClient
from karp_red_api_client.api import querying
from returns.result import Failure, Success

app = typer.Typer(help="Karp Red API client")


@app.command()
def query(
    resources: list[str],
    output: t.Annotated[Path | None, typer.Option(help="Output to this path")] = None,
    hits: t.Annotated[bool, typer.Option(help="Only output the hits")] = False,
    size: t.Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Query the given resources."""
    if isinstance(output, Path):
        output.parent.mkdir(exist_ok=True, parents=True)

    client = RedClient()

    match querying.query_sync(",".join(resources), client=client, query_options=querying.QueryOptions(size=size)):
        case Success(resp):
            if resp.parsed is None:
                print("No response", file=sys.stderr)  # noqa: T201
                return
            if hits:
                json_arrays.dump_to_file(
                    (hit.to_dict() for hit in resp.parsed.hits), output, use_stdout_as_default=True
                )
            else:
                json_arrays.dump_to_file(resp.parsed.to_dict(), output, use_stdout_as_default=True)
        case Failure(err):
            print(f"Error occurred!\n{err}", file=sys.stderr)  # noqa: T201
            sys.exit(2)
