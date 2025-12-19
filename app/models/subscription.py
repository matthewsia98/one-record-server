from __future__ import annotations

from datetime import datetime
from typing import Optional, override

from fastapi import Depends
from pydantic import (
    AnyUrl,
    BaseModel,
    SerializationInfo,
    field_validator,
    model_serializer,
)
from rdflib import RDF, XSD, BNode, Graph, Literal, URIRef

from app.dependencies.graph import parse_graph
from app.models.common import IRI, Graphable
from app.namespaces._API import API
from app.namespaces._CARGO import CARGO


def validate_topic_type(value: AnyUrl) -> AnyUrl:
    print(f"Validating topic_type: {value}")
    topic_type = URIRef(str(value))
    if topic_type not in {
        API.LOGISTICS_OBJECT_TYPE,
        API.LOGISTICS_OBJECT_IDENTIFIER,
    }:
        raise ValueError(
            f"topic_type must be either {API.LOGISTICS_OBJECT_TYPE} or {API.LOGISTICS_OBJECT_IDENTIFIER}"
        )
    return AnyUrl(str(topic_type))


class Subscription(BaseModel, Graphable):
    id: IRI
    subscriber: IRI
    topic_type: IRI
    topic: str
    description: Optional[str] = None
    expires_at: Optional[datetime] = None
    send_lo_body: Optional[bool] = None
    include_subscription_event_type: Optional[str] = None
    notify_request_status_change: Optional[bool] = None

    @field_validator("topic_type")
    def check_topic_type(cls, v: IRI) -> IRI:
        allowed = {
            str(API.LOGISTICS_OBJECT_TYPE),
            str(API.LOGISTICS_OBJECT_IDENTIFIER),
        }
        if str(v) not in allowed:
            raise ValueError(f"topic_type must be one of {allowed}")
        return v

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Subscription:
        return Subscription(
            id=IRI(""),
            subscriber=IRI(""),
            topic_type=IRI(""),
            topic="",
        )

    @override
    def to_graph(self) -> Graph:
        node = BNode(str(self.id))
        g = Graph(bind_namespaces="none")
        g.bind("cargo", CARGO._NS)
        g.bind("api", API._NS)

        g.add((node, RDF.type, API.Subscription))
        # g.add((node, API.hasContentType, Literal(content_type)))
        g.add(
            (
                node,
                API.hasSubscriber,
                URIRef(str(self.subscriber)),
            )
        )
        g.add((node, API.hasTopicType, URIRef(str(self.topic_type))))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_UPDATED))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_OBJECT_CREATED))
        g.add((node, API.includeSubscriptionEventType, API.LOGISTICS_EVENT_RECEIVED))
        g.add((node, API.hasTopic, Literal(self.topic, datatype=XSD.anyURI)))

        return g

    @model_serializer(mode="plain")
    def serialize_model(self, info: SerializationInfo):
        if info.context is not None:
            format = info.context.get("format", "json-ld")
        else:
            format = "json-ld"
        # content_type = rdflib.util.FORMAT_MIMETYPE_MAP.get(format)[0]

        g = self.to_graph()

        return g.serialize(
            format=format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
            },
        )
