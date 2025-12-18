from devtools import debug
from fastapi import APIRouter, Depends, Response, status
from rdflib import Graph

from app.dependencies.graph import parse_graph

router = APIRouter()


@router.post(
    "/logistics-objects/{logistics_object_id}/logistics-events",
    tags=["logistics-events"],
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
async def receive_logistics_event(
    logistics_object_id: str,
    g: Graph = Depends(parse_graph),
):
    debug(logistics_object_id)
    debug(g.serialize(format="json-ld"))

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
