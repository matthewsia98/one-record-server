"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/server-information/
"""

import orjson
import pyld
from fastapi import APIRouter, Header, Request, Response
from pydantic import AnyUrl
from rdflib import URIRef
from rdflib.util import FORMAT_MIMETYPE_MAP

from app.models.server_information import ServerInformation
from app.namespaces import API

router = APIRouter()

SERVER_INFORMATION_RESPONSE_HEADERS = {
    "Content-Type": {
        "description": "The content type that is contained with the HTTP body.",
        "schema": {
            "type": "string",
            "example": "application/ld+json",
        },
    },
    "Content-Language": {
        "description": "Describes the language(s) for which the requested resource is intended.",
        "schema": {
            "type": "string",
            "example": "en-US",
        },
    },
    "Last-Modified": {
        "description": "The date and time of the most recent change to the server information. See https://developer.mozilla.org/en-US/docs/Web/",
        "schema": {
            "type": "string",
            "example": "Tue, 21 Feb 2023 07:28:00 GMT",
        },
    },
}


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/server-information/#endpoint
@router.get(
    "/",
    tags=["server-information"],
    response_class=Response,
    responses={
        200: {
            "description": "The request to retrieve the ServerInformation has been successful",
            "headers": SERVER_INFORMATION_RESPONSE_HEADERS,
        },
        301: {
            "description": " Indicate that the server has moved permanently to a new location",
        },
        401: {
            "description": "Not authenticated or expired token",
        },
        403: {
            "description": "Not authorized to perform action",
        },
        404: {
            "description": "Resource Not Found",
        },
        405: {
            "description": "Method not allowed",
        },
        415: {
            "description": "Unsupported content type",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def get_server_information(
    request: Request,
    accept: str = Header(
        alias="Accept",
        description=" 	The content type that you want the HTTP response to be formatted in.",
        openapi_examples={
            "application/ld+json": {"value": "application/ld+json"},
        },
    ),
):
    # response_type, _, version = accept.partition(";")
    # response_type = response_type.strip()
    # version = version.strip()

    # serialization_format = None
    # for short, long in rdflib.util.FORMAT_MIMETYPE_MAP.items():
    #     if long[0] == response_type:
    #         serialization_format = short
    #         break
    # if serialization_format is None:
    #     return Response(
    #         content="Unsupported Accept header",
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #     )

    # serialization_format = "json-ld"
    # response_type = "application/ld+json"

    base_url = str(request.base_url)
    server_endpoint = AnyUrl(base_url)
    data_holder = URIRef(f"{base_url}/logistics-objects/_data-holder")

    server_information = ServerInformation(
        has_data_holder=data_holder,
        has_server_endpoint=server_endpoint,
        has_supported_api_version={
            "2.2.0",
        },
        has_supported_content_type={
            mt for mts in FORMAT_MIMETYPE_MAP.values() for mt in mts
        },
        has_supported_language={
            "en-US",
        },
        has_supported_ontology={
            URIRef("https://onerecord.iata.org/ns/cargo/3.2.0"),
            URIRef("https://onerecord.iata.org/ns/api/2.2.0"),
        },
    )

    g = server_information.to_graph()
    serialized = g.serialize(format="json-ld")
    FRAME = {
        "@context": {
            "@vocab": str(API._NS),
        },
        "@type": str(API.ServerInformation),
        "@embed": "@always",
    }
    framed = pyld.jsonld.frame(orjson.loads(serialized), FRAME)
    compacted = pyld.jsonld.compact(framed, FRAME)

    return Response(
        headers={
            "Content-Type": "application/ld+json",
            "Content-Language": "en-US",
        },
        content=orjson.dumps(compacted),
    )
