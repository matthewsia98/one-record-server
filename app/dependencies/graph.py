"""
Docstring for app.dependencies.graph
"""

from fastapi import Body, Header
from rdflib import Graph


def parse_graph(
    body_bytes: bytes = Body(...),
    content_type: str = Header(
        ...,
        alias="Content-Type",
    ),
) -> Graph:
    # content_type = request.headers.get("content-type")

    # if content_type is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Content-Type header is missing",
    #     )

    # if not content_type.startswith("application/ld+json"):
    #     raise HTTPException(
    #         status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    #         detail="Content-Type must be application/ld+json",
    #     )

    # body_bytes = await request.body()

    g = Graph()

    g.parse(data=body_bytes, format="json-ld")

    return g.skolemize(
        authority="http://tc.gc.ca/",
        basepath="/pact/one-record-server/",
    )
