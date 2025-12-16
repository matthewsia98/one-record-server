"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/
"""

from fastapi import APIRouter, Depends, Response, Header, status
import rdflib.util
from rdflib import Graph
from _API import API
from _CARGO import CARGO
from app.dependencies.graph import parse_graph

router = APIRouter()


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/#send-notification
@router.post(
    "/notifications",
    tags=["notifications"],
    response_class=Response,
    responses={
        204: {"description": "The request has been successful"},
        400: {"description": "Notification format is invalid"},
        401: {"description": "Not authenticated, invalid or expired token"},
        403: {"description": "Not authorized to perform action"},
        404: {"description": "Resource Not Found"},
        405: {"description": "Method not allowed"},
        415: {"description": "Unsupported content type"},
        500: {"description": "Internal Server Error"},
    },
)
async def receive_notification(
    accept: str = Header(
        alias="Accept",
        description="The content type in which the ONE Record client wants the HTTP response formatted.",
        example="application/ld+json",
    ),
    g: Graph = Depends(parse_graph),
):
    response_type, _, version = accept.partition(";")
    response_type = response_type.strip()
    version = version.strip()

    serialization_format = "json-ld"
    for short, long in rdflib.util.FORMAT_MIMETYPE_MAP.items():
        if long[0] == response_type:
            serialization_format = short
            break

    print(
        "Received Notification:\n",
        g.serialize(
            format=serialization_format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
            },
        ),
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
