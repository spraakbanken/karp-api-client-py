"""Karp API client command-line."""

import sys

from karp_api_client.cli import red_app

try:
    import typer
except ImportError:
    print("please install this package with the optional cli, e.g. `karp-api-client[cli]`")  # noqa: T201
    sys.exit(1)

app = typer.Typer(help="Karp API client")

app.add_typer(red_app.app, name="red")
