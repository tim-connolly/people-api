"""Type definitions for the GraphQL schema."""

from enum import Enum

import strawberry


@strawberry.enum(description="A geographical state located within Australia.")
class State(Enum):
    ACT = strawberry.enum_value("ACT", description="Australian Capital Territory")
    NSW = strawberry.enum_value("NSW", description="New South Wales")
    NT = strawberry.enum_value("NT", description="Northern Territory")
    QLD = strawberry.enum_value("QLD", description="Queensland")
    SA = strawberry.enum_value("SA", description="South Australia")
    TAS = strawberry.enum_value("TAS", description="Tasmania")
    VIC = strawberry.enum_value("VIC", description="Victoria")
    WA = strawberry.enum_value("WA", description="Western Australia")


@strawberry.type(description="A street address.")
class Address:
    number: int = strawberry.field(description="The street number of this address.")
    street: str = strawberry.field(
        description="Street name and type (eg. Ocean Avenue)."
    )
    city: str = strawberry.field(description="The city this address is located within.")
    state: State = strawberry.field(
        description="The state this address is located within."
    )


@strawberry.type(description="Details about a person.")
class Person:
    name: str = strawberry.field(description="The name of this person.")
    email: str = strawberry.field(description="The email address of this person.")
    address: Address = strawberry.field(description="The home address of this person.")
