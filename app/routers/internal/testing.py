import rdflib.util
from fastapi import (
    APIRouter,
    Depends,
    Header,
    Response,
)
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.namespaces._API import API
from app.namespaces._CARGO import CARGO

router = APIRouter()


@router.post("/internal/echo", tags=["internal"])
async def echo(accept: str = Header(...), g: Graph = Depends(parse_graph)):
    response_type, _, version = accept.partition(";")
    response_type = response_type.strip()
    version = version.strip()

    serialization_format = "json-ld"
    for short, long in rdflib.util.FORMAT_MIMETYPE_MAP.items():
        if long[0] == response_type:
            serialization_format = short
            break
    return Response(
        content=g.serialize(
            format=serialization_format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
            },
        ),
        media_type=response_type,
    )
