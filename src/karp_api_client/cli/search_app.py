"""Karp API client command-line."""

import datetime
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
    size: t.Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Search the given resources."""
    datetime_now = datetime.datetime.now()
    default_filename = f"karp-search-search-{datetime_now.strftime('%Y-%m-%dT%H:%M:%S')}.jsonl"
    if output is None:
        output = Path(f"output/{default_filename}")
    elif output.is_dir():
        output /= default_filename

    print(f"Output will be written to '{output}'", file=sys.stderr)  # noqa: T201
    output.parent.mkdir(exist_ok=True, parents=True)

    client = SearchClient()
    search_options = searching.SearchOptions(resources=resources, size=size)
    response = searching.search_sync(client=client, search_options=search_options)

    match response:
        case Success(resp):
            if resp.parsed is None:
                print("No response", file=sys.stderr)  # noqa: T201
                return
            json_arrays.dump_to_file((hit.to_dict() for hit in resp.parsed.hits), output)
        case Failure(err):
            print(f"Error occurred!\n{err}", file=sys.stderr)  # noqa: T201
            sys.exit(2)
