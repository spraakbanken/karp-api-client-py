"""Example using this library in sync code."""

import sys

from karp_red_api_client import RedClient, dsl
from karp_red_api_client.api import querying
from karp_red_api_client.models import QueryResponse
from karp_red_api_client.responses import Response
from returns.result import Failure, Success


def main() -> None:  # noqa: D103
    client = RedClient()

    with client as client:
        q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
        response = querying.query_sync(
            "schlyter,soederwall,soederwall-supp",
            client=client,
            query_options=querying.QueryOptions(size=25, q=q),
        )
        match response:
            case Success(resp):
                _print_table(resp)
            case Failure(err):
                print(f"Error occurred!\n{err}")  # noqa: T201
                sys.exit(2)


def _print_table(response: Response[QueryResponse]) -> None:
    if response.parsed is None:
        print("No response")  # noqa: T201
        return
    print(f"{'baseform':20s}{'resource':20s}entry")  # noqa: T201
    for entry in response.parsed.hits:
        print(f"{entry.entry['baseform']:20s}{entry.resource:20s}{entry.to_dict()}")  # noqa: T201

    print("---")  # noqa: T201
    print(f"showing {len(response.parsed.hits)} entries of {response.parsed.total} in total.")  # noqa: T201


if __name__ == "__main__":
    main()
