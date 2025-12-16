from fastapi import (
    Depends,
    Request,
    Response,
    APIRouter,
)
import rdflib.util
from rdflib import Graph
from _API import API
from _CARGO import CARGO
from app.dependencies.graph import parse_graph

router = APIRouter()


@router.post("/echo", tags=["testing"])
async def echo(request: Request, g: Graph = Depends(parse_graph)):
    response_type, version = request.headers.get("accept").split(";", 1)
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
