"""GraphQL schema definition."""

from typing import List

import strawberry
from strawberry.asgi import GraphQL

from .data import STORED_PEOPLE
from .types import Address
from .types import Person


@strawberry.type(description="People API queries.")
class Query:
    @strawberry.field(description="Get details for all people.")
    def people(self) -> List[Person]:
        return [
            Person(
                name=p["name"],
                email=p["email"],
                address=Address(
                    number=p["address"]["number"],
                    street=p["address"]["street"],
                    city=p["address"]["city"],
                    state=p["address"]["state"],
                ),
            )
            for p in STORED_PEOPLE
        ]


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)
