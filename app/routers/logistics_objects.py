"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/logistics-objects/
"""

from datetime import datetime

from devtools import debug
from fastapi import APIRouter, Depends, Header, Query, Request, Response, status
from rdflib import RDF, URIRef

from app.dependencies.datetime import parse_datetime_param
from app.models.logistics_object import LogisticsObject
from app.models.organization import Organization
from app.namespaces._CARGO import CARGO

router = APIRouter()

LOGISTICS_OBJECTS_RESPONSE_HEADERS = {
    "Location": {
        "description": "The URI of the newly created Logistics Object",
        "required": True,
        "schema": {"type": "string", "format": "uri"},
    },
    "Type": {
        "description": "The type of the newly created Logistics Object as a URI",
        "required": True,
        "schema": {"type": "string", "format": "uri"},
    },
}


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/logistics-objects/#create-a-logistics-object
@router.post(
    "/logistics-objects",
    tags=["logistics-objects"],
    status_code=status.HTTP_201_CREATED,
    # openapi_extra={
    #     "requestBody": {
    #         "content": {
    #             "application/ld+json": {
    #                 "schema": {"$ref": "#/components/schemas/LogisticsObject"},
    #             }
    #         }
    #     }
    # },
    response_class=Response,
    responses={
        201: {
            "description": "Logistics Object has been created",
            "headers": LOGISTICS_OBJECTS_RESPONSE_HEADERS,
        },
        400: {
            "description": "Invalid Logistics Object",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #     }
            # },
        },
        401: {
            "description": "Not authenticated",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        403: {
            "description": "Not authorized to publish the Logistics Object to the server",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        409: {
            "description": "Logistics object with specified ID already exists",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        415: {
            "description": "Unsupported Content Type",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        500: {
            "description": "Internal Server Error",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
    },
)
async def receive_logistics_object(
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
    # _doc_body: LogisticsObject = Body(...),
    logistics_object: LogisticsObject = Depends(LogisticsObject.from_graph),
):
    debug(logistics_object.iri)
    debug(logistics_object.graph.serialize())

    logistics_object_type = logistics_object.graph.value(
        URIRef(str(logistics_object.iri)), RDF.type
    )

    match logistics_object_type:
        case CARGO.Shipment:
            debug("It's a shipment")
        case CARGO.Piece:
            debug("It's a piece")
        case _:
            debug(logistics_object_type)

    return Response(
        status_code=status.HTTP_201_CREATED,
    )


@router.get(
    "/logistics-objects/{logistics_object_id}",
    tags=["logistics-objects"],
)
async def get_logistics_object(
    logistics_object_id: str,
    request: Request,
    embedded: bool = Query(
        default=False,
        description="Optional parameter that can be used to request an embedded version of a Logistics Object, if the parameter is not set, a linked version of the Logistics Object is returned",
    ),
    at: datetime = Depends(
        parse_datetime_param(
            param_name="at",
            description="Optional parameter that can be used to request a historical version of Logistics Object, if the parameter is not set, the latest version is returned",
        )
    ),
):
    debug(logistics_object_id)
    debug(embedded)
    debug(at)

    if logistics_object_id == "_data-holder":
        g = Organization(name="ACME Corporation").to_graph()
        g = g.skolemize(
            authority=str(request.base_url),
            basepath="logistics-objects/",
        )

        return Response(
            status_code=status.HTTP_200_OK,
            content=g.serialize(
                format="json-ld",
                context={
                    "@vocab": CARGO._NS,
                },
            ),
        )

    return Response(
        status_code=status.HTTP_200_OK,
    )
