"""Karp API client command-line."""

import datetime
import sys
from typing import Annotated, Optional

import json_arrays

from karp_api_client import Client
from karp_api_client.api import querying
from karp_api_client.models.http_validation_error import HttpValidationError
from karp_api_client.shared import Response

try:
    import typer
except ImportError:
    print("please install this package with the optional cli, e.g. `karp-api-client[cli]`")  # noqa: T201
    sys.exit(1)

app = typer.Typer(help="Karp API client")


@app.command()
def query(
    resources: list[str],
    output: Annotated[str | None, typer.Option(help="Output to this path")] = None,
    size: Annotated[int | None, typer.Option(help="The number of hits requested")] = None,
) -> None:
    """Query the given resources."""
    if output is None:
        output = f"karp-query-{datetime.datetime.now()}.jsonl"
        print(f"Output will be written to '{output}'", file=sys.stderr)  # noqa: T201
    json_dumper = Dumper(output=output)
    client = Client()
    response = querying.query_sync(",".join(resources), client=client, query_options=querying.QueryOptions(size=size))

    response.map(json_dumper).alt(_print_error)
    # TODO: use python 3.10 syntax when python 3.9 support is dropped.
    # match response:
    #     case Success(resp):
    #         if resp.parsed is None:
    #             print("No response", file=sys.stderr)
    #             return
    #         json_arrays.dump_to_file((hit.to_dict() for hit in resp.parsed.hits), output)
    #     case Failure(err):
    #         print(f"Error occurred!\n{err}", file=sys.stderr)
    #         sys.exit(2)


class Dumper:
    """Adapter to write successful response to given output."""

    def __init__(self, output: str) -> None:
        self.output = output

    def __call__(self, response: Response) -> None:
        """Dump the response to a file."""
        if response.parsed is None:
            print("No response", file=sys.stderr)  # noqa: T201
            return
        json_arrays.dump_to_file((hit.to_dict() for hit in response.parsed.hits), self.output)


def _print_error(err: Response[Optional[HttpValidationError]]) -> None:
    print(f"Error occurred!\n{err}", file=sys.stderr)  # noqa: T201
    sys.exit(2)
