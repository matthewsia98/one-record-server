"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/server-information/
"""

from fastapi import APIRouter, Header, Response

from app.models.common import IRI
from app.models.server_information import ServerInformation

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

    serialization_format = "json-ld"
    response_type = "application/ld+json"

    server_information = ServerInformation(
        has_data_holder=IRI(
            "https://1r.example.com/logistics-objects/957e2622-9d31-493b-8b8f-3c805064dbda"
        ),
        has_server_endpoint=IRI("http://1r.example.com"),
        has_supported_api_version={
            "2.2.0",
        },
        has_supported_content_type={
            "application/ld+json",
        },
        has_supported_language={
            "en-US",
        },
        has_supported_ontology={
            IRI("https://onerecord.iata.org/ns/cargo/3.2.0"),
            IRI("https://onerecord.iata.org/ns/api/2.2.0"),
        },
    )

    return Response(
        headers={
            "Content-Type": response_type,
            "Content-Language": "en-US",
        },
        content=server_information.model_dump(
            context={
                "format": serialization_format,
            }
        ),
    )
