from pydantic import (
    BaseModel,
    Field,
    PlainValidator,
    model_serializer,
    SerializationInfo,
)
from rdflib import RDF, XSD, BNode, Graph, Literal, URIRef
from typing import Annotated, Any, Optional

import rdflib.util
from _API import API
from datetime import datetime

from _CARGO import CARGO


def validate_topic_type(value: Any) -> URIRef:
    topic_type = URIRef(value)
    if topic_type not in {
        API.LOGISTICS_OBJECT_TYPE,
        API.LOGISTICS_OBJECT_IDENTIFIER,
    }:
        raise ValueError(
            f"topic_type must be either {API.LOGISTICS_OBJECT_TYPE} or {API.LOGISTICS_OBJECT_IDENTIFIER}"
        )
    return topic_type


class Subscription(BaseModel):
    id: URIRef
    subscriber: URIRef
    topic_type: Annotated[URIRef, Field(PlainValidator(validate_topic_type))]
    topic: str
    description: Optional[str] = None
    expires_at: Optional[datetime] = None
    send_lo_body: Optional[bool] = None
    include_subscription_event_type: Optional[str] = None
    notify_request_status_change: Optional[bool] = None

    model_config = {
        "arbitrary_types_allowed": True,
    }

    @model_serializer(mode="plain")
    def serialize_model(self, info: SerializationInfo) -> str:
        format = info.context.get("format", "json-ld")
        content_type = rdflib.util.FORMAT_MIMETYPE_MAP.get(format)[0]

        node = BNode(self.id)
        g = Graph(bind_namespaces="none")
        g.bind("cargo", CARGO._NS)
        g.bind("api", API._NS)

        g.add((node, RDF.type, API.Subscription))
        g.add((node, API.hasContentType, Literal(content_type)))
        g.add(
            (
                node,
                API.hasSubscriber,
                URIRef(
                    "https://1r.example.com/logistics-objects/957e2622-9d31-493b-8b8f-3c805064dbda"
                ),
            )
        )
        g.add((node, API.hasTopicType, URIRef(self.topic_type)))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_UPDATED))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_CREATED))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_EVENT_RECEIVED))
        g.add((node, API.hasTopic, Literal(self.topic, datatype=XSD.anyURI)))

        return g.serialize(
            format=format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
            },
        )
