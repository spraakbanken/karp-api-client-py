"""Karp API client command-line."""

import sys
import typing as t
from pathlib import Path

import json_arrays
import typer
from karp_red_api_client import Client as RedClient
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import HTTPValidationError
from karp_red_api_client.types import UNSET

app = typer.Typer(help="Karp Red API client")


@app.command(name="query")
def query_cmd(
    resources: list[str],
    output: t.Annotated[Path | None, typer.Option(help="Output to this path")] = None,
    hits: t.Annotated[bool, typer.Option(help="Only output the hits")] = False,
    size: t.Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Query the given resources."""
    if isinstance(output, Path):
        output.parent.mkdir(exist_ok=True, parents=True)

    client = RedClient()

    resp = query.sync_detailed(client=client, resources=resources, size=size if size is not None else UNSET)
    if resp.status_code.is_success:
        if resp.parsed is None:
            print("No response", file=sys.stderr)  # noqa: T201
            return
        if isinstance(resp.parsed, HTTPValidationError):
            print(f"Error occurred!\n{resp.parsed}", file=sys.stderr)  # noqa: T201
            sys.exit(1)
        if hits:
            json_arrays.dump_to_file((hit.to_dict() for hit in resp.parsed.hits), output, use_stdout_as_default=True)
        else:
            json_arrays.dump_to_file(resp.parsed.to_dict(), output, use_stdout_as_default=True)
    else:
        print(f"Error occurred!\n{resp.parsed}", file=sys.stderr)  # noqa: T201
        sys.exit(2)
