"""The application entry-point."""

from fastapi import FastAPI

import people_api as package
from .graphql import graphql_app


app = FastAPI(
    title="People API", version=package.__version__, description=package.__doc__
)
app.add_route("/graphql", graphql_app)
