# karp-client-py

Karp API Client

> [!NOTE]
> This project is under development

## Installation

To add this package to your project

```shell
uv add git+https://github.com/spraakbanken/karp-api-client-py
```

### Optional cli

By installing the optional group `cli`, you can also use this library as a cli `karp-client`.

```shell
pip install 'git+https://github.com/spraakbanken/karp-api-client-py[cli]'
```

Call the API:

```shell
karp-client <RESOURCE1> [<RESOURCE2>...] --size <MAX_NUM_HITS>
```

## Usage

Use this library in sync code:

```python
from karp_red_api_client import Client, dsl
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import QueryResponse


def main() -> None:
    client = Client()

    with client as client:
        q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
        response = query.sync_detailed(
            "schlyter,soederwall,soederwall-supp",
            client=client,
            q=q,
            size=25,
        )
        if response.status_code.is_success and isinstance(response.parsed, QueryResponse):
            _print_table(resp.parsed)
        else:
            print(f"Error occurred!\n{err}")


def _print_table(response: QueryResponse) -> None:
    print(f"{'baseform':20s}{'resource':20s}entry")
    for entry in response.hits:
        print(f"{entry['entry']['baseform']:20s}{entry['resource']:20s}{entry}")

    print("---")
    print(f"showing {len(response.hits)} entries of {response.total} in total.")


if __name__ == "__main__":
    main()
```

Or use it in async code:

```python
import anyio

from karp_red_api_client import Client, dsl
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import QueryResponse


async def main():
    client = Client()

    async with client as client:
        q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
        response = await query.asyncio_detailed(
            "schlyter,soederwall,soederwall-supp",
            client=client,
            q=q,
            size=25,
        )
        if response.status_code.is_success and isinstance(response.parsed, QueryResponse):
            _print_table(resp.parsed)
        else:
            print(f"Error occurred!\n{err}")


def _print_table(response: QueryResponse) -> None:
    print(f"{'baseform':20s}{'resource':20s}entry")
    for entry in response.hits:
        print(f"{entry['entry']['baseform']:20s}{entry['resource']:20s}{entry}")

    print("---")
    print(f"showing {len(response.hits)} entries of {response.total} in total.")


if __name__ == "__main__":
    anyio.run(main)
```

## Roadmap

- [ ] Karp Query DSL
  - [ ] Query operators
    - [ ] `contains|<field>|<string>`
    - [ ] `endswith|<field>|<string>`
    - [x] `equals|<field>|<string>`
    - [ ] `exists|<field>`
    - [ ] `freetext|<string>`
    - [ ] `gt|<field>|<value>`
    - [ ] `gte|<field>|<value>`
    - [ ] `lt|<field>|<value>`
    - [ ] `lte|<field>|<value>`
    - [ ] `missing|<field>`
    - [ ] `regexp|<field>|<regex.*>`
    - [ ] `startswith|<field>|<string>`
  - [ ] Logical operators
    - [ ] `not(<expr1>||<expr2>||...)`
    - [ ] `and(<expr1>||<expr2>||...)`
    - [x] `or(<expr1>||<expr2>||...)`
  - [ ] Karp Red Query DSL
    - [ ] Subqueries
- [ ] Karp Red API Calls
  - [ ] Searching
    - [x] `/query/{resources}`
    - [ ] `/query/stats/{resources}`
    - [ ] `/query/entries/{resource_id}/{entry_ids}`
  - [ ] Editing
  - [ ] Statistics
  - [ ] History
  - [ ] Resources
  - [ ] Default
- [ ] Karp Search API Calls

## Development

Both [`karp-red-api-client`](./karp-red-api-client) and [`karp-search-api-client`](./karp-search-api-client) are generated with [openapi-generators/openapi-python-client](https://github.com/openapi-generators/openapi-python-client). And both depend on a common library, [`karp-api-core`](./karp-api-core) with common classes.

### Custom templates

The folder [templates](./templates) contains the templates used (copied from `openapi-python-client`) and modified to use `karp_api_core`.

### Query DSL

The query dsl is currently 2 copies in both `karp-red-api-client` and `karp-search-api-client`, but all common code should be implemented in `karp-api-core`.

### Nuvarande problem i Karp Red API

`openapi-python-client` har problem med 12 st anrop i Karp Red API, behöver kolla närmare var problemet är, hos `openapi-python-client` eller i `karp-red-backend`:s specifikation?
