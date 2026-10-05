"""Karp API client command-line."""

import sys
import typing as t
from pathlib import Path

import json_arrays
import typer
from karp_search_api_client import Client as SearchClient
from karp_search_api_client.api.default import do_search_search_get
from karp_search_api_client.types import UNSET

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

    resp = do_search_search_get.sync_detailed(client=client, resources=resources, size=size or UNSET)

    if resp.status_code.is_success:
        if resp.parsed is None:
            print("No response", file=sys.stderr)  # noqa: T201
            return
        if hits:
            json_arrays.dump_to_file((hit.to_dict() for hit in resp.parsed.hits), output, use_stdout_as_default=True)
        else:
            json_arrays.dump_to_file(resp.parsed.to_dict(), output, use_stdout_as_default=True)
    else:
        print(f"Error occurred!\n{resp.parsed}", file=sys.stderr)  # noqa: T201
        sys.exit(2)
