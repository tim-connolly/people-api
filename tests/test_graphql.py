"""Test querying the GraphQL endpoint."""

import pytest

from people_api.data import STORED_PEOPLE
from people_api.graphql import schema

pytestmark = pytest.mark.asyncio


async def test_query():
    """Test if the default query returns the expected stored data."""

    query = """
        query {
          people {
            email
            name
            address {
              number
              street
              city
              state
            }
          }
        }
    """

    result = await schema.execute(query)

    assert result.errors is None
    assert result.data["people"] == STORED_PEOPLE
