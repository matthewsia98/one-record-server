"""
Docstring for app.dependencies.graph
"""

from fastapi import Request, HTTPException, status
from rdflib import Graph


async def parse_graph(request: Request) -> Graph:
    content_type = request.headers.get("content-type")

    if content_type is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Content-Type header is missing",
        )

    if not content_type.startswith("application/ld+json"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Content-Type must be application/ld+json",
        )

    body_bytes = await request.body()

    g = Graph()

    g.parse(data=body_bytes, format="json-ld")

    return g
