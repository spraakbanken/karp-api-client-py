"""Example of using this library in async code."""

import sys

import anyio
from karp_red_api_client import Client, dsl
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import QueryResponse


async def main() -> None:  # noqa: D103
    client = Client()

    q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
    response = await query.asyncio_detailed(
        resources="schlyter,soederwall,soederwall-supp",
        client=client,
        q=q,
        size=25,
    )
    if response.status_code.is_success and isinstance(response.parsed, QueryResponse):
        _print_table(response.parsed)
    else:
        print(f"Error occurred!\n{response.parsed}")  # noqa: T201
        sys.exit(2)


def _print_table(response: QueryResponse) -> None:
    print(f"{'baseform':20s}{'resource':20s}entry")  # noqa: T201
    for entry in response.hits:
        print(f"{entry.entry['baseform']:20s}{entry.resource:20s}{entry.to_dict()}")  # noqa: T201

    print("---")  # noqa: T201
    print(f"showing {len(response.hits)} entries of {response.total} in total.")  # noqa: T201


if __name__ == "__main__":
    anyio.run(main)
