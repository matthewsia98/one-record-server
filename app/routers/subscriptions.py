"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/subscriptions/
"""

from fastapi import APIRouter, Response, Query, Header, status
import rdflib.util
from rdflib import Graph, RDF, BNode, Literal, URIRef, XSD
from _API import API
from _CARGO import CARGO

router = APIRouter()

SUBSCRIPTIONS_RESPONSE_HEADERS = {
    "Content-Type": {
        "description": "The content type that is contained with the HTTP body.",
        "schema": {"type": "string"},
    },
    "Content-Language": {
        "description": "Describes the language(s) for which the requested resource is intended.",
        "schema": {"type": "string"},
    },
}


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/subscriptions/#endpoint
@router.get(
    "/subscriptions",
    tags=["subscriptions"],
    response_class=Response,
    responses={
        200: {
            "description": "The request to retrieve the Subscription Information has been successful",
            # "headers": SUBSCRIPTIONS_RESPONSE_HEADERS,
            "content": {
                "application/ld+json": {
                    "example": {
                        "@context": {
                            "cargo": "https://onerecord.iata.org/ns/cargo#",
                            "api": "https://onerecord.iata.org/ns/api#",
                        },
                        "@id": "https://1r.example.com/subscriptions/5f1a4869-e324-45b1-9ab0-60271ba54185",
                        "@type": "api:Subscription",
                        "api:hasContentType": "application/ld+json",
                        "api:hasSubscriber": {
                            "@id": "https://1r.example.com/logistics-objects/957e2622-9d31-493b-8b8f-3c805064dbda"
                        },
                        "api:hasTopicType": {"@id": "api:LOGISTICS_OBJECT_IDENTIFIER"},
                        "api:includeSubscriptionEventType": [
                            {"@id": "api:LOGISTICS_OBJECT_UPDATED"},
                            {"@id": "api:LOGISTICS_OBJECT_CREATED"},
                            {"@id": "api:LOGISTICS_EVENT_RECEIVED"},
                        ],
                        "api:hasTopic": {
                            "@type": "http://www.w3.org/2001/XMLSchema#anyURI",
                            "@value": "https://1r.example.com/logistics-objects/1a8ded38-1804-467c-a369-81a411416b7c",
                        },
                    }
                }
            },
        },
        400: {
            "description": "The request is invalid",
            # "headers": SUBSCRIPTIONS_RESPONSE_HEADERS,
        },
        401: {
            "description": "Not authenticated",
            # "headers": SUBSCRIPTIONS_RESPONSE_HEADERS,
        },
        403: {
            "description": "Not authorized to retrieve the Subscription Information",
        },
        500: {
            "description": "Internal server error",
            # "headers": SUBSCRIPTIONS_RESPONSE_HEADERS,
        },
    },
)
async def get_subscription_info(
    accept: str = Header(
        alias="Accept",
        description="The content type in which the ONE Record client wants the HTTP response formatted.",
        openapi_examples={
            "application/ld+json": {"value": "application/ld+json"},
            "application/ld+json; version=2.2.0": {
                "value": "application/ld+json; version=2.2.0"
            },
            "application/ld+json; version=1.2": {
                "value": "application/ld+json; version=1.2"
            },
        },
    ),
    topic_type: str = Query(
        alias="topicType",
        description="Used by the publisher to specify if Subscription information for a specific Logistics Object or a data class should be in the response body. When passed in a URL, the topicType must be URL encoded (i.e # becomes %23 or can be replaced with /)",
        openapi_examples={
            "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_TYPE": {
                "value": "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_TYPE"
            },
            "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_IDENTIFIER": {
                "value": "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_IDENTIFIER"
            },
        },
    ),
    topic: str = Query(
        description="Used by the publisher to specify the data class or Logistics Object URI the Subscription information should be related to. topic MUST be a valid URI",
        openapi_examples={
            "https://onerecord.iata.org/ns/cargo#Piece": {
                "value": "https://onerecord.iata.org/ns/cargo#Piece"
            },
            "https://1r.example.com/logistics-objects/1a8ded38-1804-467c-a369-81a411416b7c": {
                "value": "https://1r.example.com/logistics-objects/1a8ded38-1804-467c-a369-81a411416b7c"
            },
        },
    ),
):
    response_type, _, version = accept.partition(";")
    response_type = response_type.strip()
    version = version.strip()

    serialization_format = None
    for short, long in rdflib.util.FORMAT_MIMETYPE_MAP.items():
        if long[0] == response_type:
            serialization_format = short
            break
    if serialization_format is None:
        return Response(
            content="Unsupported Accept header",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    node = BNode(
        "https://1r.example.com/subscriptions/5f1a4869-e324-45b1-9ab0-60271ba54185"
    )
    g = Graph(bind_namespaces="none")
    g.bind("cargo", CARGO._NS)
    g.bind("api", API._NS)

    g.add((node, RDF.type, API.Subscription))
    g.add((node, API.hasContentType, Literal(response_type)))
    g.add(
        (
            node,
            API.hasSubscriber,
            URIRef(
                "https://1r.example.com/logistics-objects/957e2622-9d31-493b-8b8f-3c805064dbda"
            ),
        )
    )
    g.add((node, API.hasTopicType, URIRef(topic_type)))
    g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_UPDATED))
    g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_CREATED))
    g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_EVENT_RECEIVED))
    g.add((node, API.hasTopic, Literal(topic, datatype=XSD.anyURI)))

    return Response(
        headers={
            "Content-Type": response_type,
            "Content-Language": "en-US",
        },
        content=g.serialize(
            format=serialization_format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
            },
        ),
    )
