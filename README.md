# Example People API

A simple GraphQL API that returns a list of people and their details.

---
## Installation

1. Clone the repository.
2. Change into the repository directory:-
```
$ cd people-api
```
3. Create and activate a virtualenv with [Python](https://www.python.org/) 3.8 or higher.
4. Install the required dependencies:-
```
(venv) $ pip install -r requirements.txt
```

## Running tests

Run [pytest](https://pytest.org/) to run all available tests:-
```
(venv) $ pytest
```

## Run the API server

By default the server will listen on port 8000.

The API server can be run with [uvicorn](https://www.uvicorn.org/).
```
(venv) $ uvicorn people_api.main:app
```

Alternatively, the built-in [strawberry](https://strawberry.rocks/) server can be used:-
```
(venv) $ strawberry server people_api.graphql:schema
```
This will also expose a web-based GraphQL client and API explorer at [http://localhost:8000/](http://localhost:8000/).

## Query the API

The GraphQL endpoint is exposed at `/graphql`.

To perform a query using [curl](https://curl.se/):-
```
$ curl -X POST \
    -H "Content-type: application/json" \
    -d '{"query": "query { people { email name address { number street city state } } }"}' \
    localhost:8000/graphql
```

To perform a query using [HTTPie](https://httpie.io/cli):-
```
$ http POST :8000/graphql query="query { people { email name address { number street city state } } }"
```

Alternatively, use your favourite GraphQL client and point it to [http://localhost:8000/graphql](http://localhost:8000/graphql).

Sample query:-
```
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
```
