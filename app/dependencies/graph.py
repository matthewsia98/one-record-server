"""
Docstring for app.dependencies.graph
"""

import json
from typing import TypeVar

import orjson
from devtools import debug, pprint
from fastapi import Depends, Header, HTTPException, Request, status
from rdflib import Graph

from app.models.common import Graphable
from app.utils.rdf import get_format_from_mime_type


async def parse_graph(
    request: Request,
    content_type: str = Header(
        ...,
        alias="Content-Type",
    ),
) -> Graph:
    if content_type is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Content-Type header is missing",
        )

    format = get_format_from_mime_type(content_type)
    debug(format)

    body = await request.body()

    # TODO: debug
    if format == "json-ld":
        print(
            json.dumps(
                orjson.loads(body),
                indent=4,
            )
        )
    else:
        pprint(body.decode())

    g = Graph()

    g.parse(data=body, format=format)

    return g


T = TypeVar("T", bound=Graphable)


def parse_graph_as(cls: type[T]):
    async def wrapper(graph: Graph = Depends(parse_graph)) -> T:
        return cls.from_graph(graph)

    return wrapper
