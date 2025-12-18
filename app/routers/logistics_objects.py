"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/logistics-objects/
"""

from devtools import debug
from fastapi import APIRouter, Depends, Header, Response, status
from rdflib import RDF, URIRef

from app.models.logistics_object import LogisticsObject

router = APIRouter()

LOGISTICS_OBJECTS_RESPONSE_HEADERS = {
    "Location": {
        "description": "The URI of the newly created Logistics Object",
        "schema": {"type": "string"},
    },
    "Type": {
        "description": "The type of the newly created Logistics Object as a URI",
        "schema": {"type": "string"},
    },
}


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/logistics-objects/#create-a-logistics-object
@router.post(
    "/logistics-objects",
    tags=["logistics-objects"],
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
    responses={
        201: {
            "description": "Logistics Object has been created",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        400: {
            "description": "Invalid Logistics Object",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        401: {
            "description": "Not authenticated",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        403: {
            "description": "Not authorized to publish the Logistics Object to the server",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        409: {
            "description": "Logistics object with specified ID already exists",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        415: {
            "description": "Unsupported Content Type",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        500: {
            "description": "Internal Server Error",
            # "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
    },
)
def receive_logistics_object(
    accept: str = Header(
        alias="Accept",
        description="The content type in which the ONE Record client wants the HTTP response to be formatted in.",
        openapi_examples={
            "application/ld+json": {"value": "application/ld+json"},
        },
    ),
    content_type: str = Header(
        alias="Content-Type",
        description="The content type that is contained with the HTTP body. Valid content types.",
        openapi_examples={
            "application/ld+json": {"value": "application/ld+json"},
        },
    ),
    logistics_object: LogisticsObject = Depends(LogisticsObject.from_graph),
):
    debug(logistics_object.iri)
    type = next(
        logistics_object.graph.objects(URIRef(str(logistics_object.iri)), RDF.type),
        None,
    )
    debug(type)
    debug(logistics_object.graph.serialize())

    return Response(
        status_code=status.HTTP_201_CREATED,
    )
