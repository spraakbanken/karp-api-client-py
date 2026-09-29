"""Karp API client command-line."""

import sys
import typing as t
from pathlib import Path

import json_arrays
import typer
from karp_search_api_client import SearchClient
from karp_search_api_client.api import searching
from returns.result import Failure, Success

app = typer.Typer(help="Karp Search API client")


@app.command()
def search(
    resources: list[str],
    output: t.Annotated[Path | None, typer.Option(help="Output to this path")] = None,
    hits: t.Annotated[bool, typer.Option(help="Only output the hits")] = False,
    size: t.Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Search the given resources."""
    if isinstance(output, Path):
        output.parent.mkdir(exist_ok=True, parents=True)

    client = SearchClient()

    search_options = searching.SearchOptions(resources=resources, size=size)

    match searching.search_sync(client=client, search_options=search_options):
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
