---
title: "Proof of concept: karp-client-py"
author: Kristoffer Andersson
---

# Generating API clients

Both `karp-red-api-client` and `karp-search-api-client` are generated with `openapi-python-client`.

And both depend on a common library, `karp-api-core` with common classes.

## Links

- openapi-python-client: https://github.com/openapi-generators/openapi-python-client

<!-- end_slide -->

# Using openapi-python-client

```bash
openapi-python-client generate \
    --meta uv \
    --path karp-search-spec.json \
    --output-path karp-search-api-client \
    --custom-template-path templates \
    --overwrite \
    --config karp-search-config.json
```

<!-- end_slide -->

# Custom templates

The folder `./templates` contains the templates used (copied from `openapi-python-client`) and modified to use `karp_api_core`.

<!-- end_slide -->

# Query DSL

The query dsl is currently 2 copies in both `karp-red-api-client` and `karp-search-api-client`, but all common code should be implemented in `karp-api-core`.

<!-- end_slide -->

### Nuvarande problem i Karp Red API

`openapi-python-client` har problem med 12 st anrop i Karp Red API, behöver kolla närmare var problemet är, hos `openapi-python-client` eller i `karp-red-backend`:s specifikation?

<!-- end_slide -->

# Example (sync)

```python
from karp_red_api_client import Client, dsl
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import QueryResponse


def main() -> None:
    client = Client()
    q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
    response = query.sync_detailed(
        client=client,
        resources="schlyter,soederwall,soederwall-supp",
        q=q,
    )
    if response.status_code.is_success and isinstance(response.parsed, QueryResponse):
        _print_table(resp.parsed)
    else:
        print(f"Error occurred!\n{err}")


def _print_table(response: QueryResponse) -> None:
    print(f"{'baseform':20s}{'resource':20s}entry")
    for entry in response.hits:
        print(f"{entry.entry['baseform']:20s}{entry.resource:20s}{entry}")

    print("---")
    print(f"showing {len(response.hits)} entries of {response.total} in total.")


if __name__ == "__main__":
    main()
```

<!-- end_slide -->

# Example (async)

```python
import anyio

from karp_red_api_client import Client, dsl
from karp_red_api_client.api.searching import query
from karp_red_api_client.models import QueryResponse


async def main():
    client = Client()

    q = dsl.Equals(field="baseform", value="agha") | dsl.Equals(field="baseform", value="agin")
    response = await query.asyncio_detailed(
        client=client,
        resources="schlyter,soederwall,soederwall-supp",
        q=q,
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

<!-- end_slide -->

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

<!-- end_slide -->

## Roadmap, cont.

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

<!-- end_slide -->

## Roadmap, cont.

- [ ] Karp Search API Calls
