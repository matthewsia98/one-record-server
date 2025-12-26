from __future__ import annotations

from typing import Optional, Self, Set, override

from pydantic import BaseModel, Field
from rdflib import RDF, Graph, Literal, URIRef
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.models.logistics_object import LogisticsObject
from app.namespaces._API import API


class NotificationMessage(BaseModel):
    notification: Notification
    logistics_object: Optional[LogisticsObject] = None


class Notification(Graphable):
    # subject: _SubjectType
    event_type: URIRef
    has_logistics_object_type: Optional[str] = None
    has_logistics_object: Optional[URIRef] = None
    triggered_by: Optional[URIRef] = None
    changed_properties: Set[URIRef] = Field(default_factory=set)

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        """
        Construct a Notification instance from an RDF graph.
        Assumes there is exactly one Notification in the graph.
        """
        if subject is None:
            subject = next(graph.subjects(RDF.type, API.Notification))

        match graph.value(subject, API.hasEventType):
            case URIRef(has_event_type_value):
                event_type = has_event_type_value
            case _:
                raise ValueError("Notification is missing hasEventType")

        has_logistics_object_type: Optional[str]
        match graph.value(subject, API.hasLogisticsObjectType):
            case Literal(has_logistics_object_type_value):
                has_logistics_object_type = str(has_logistics_object_type_value)
            case _:
                has_logistics_object_type = None

        has_logistics_object: Optional[URIRef]
        match graph.value(subject, API.hasLogisticsObject):
            case URIRef(has_logistics_object_value):
                has_logistics_object = has_logistics_object_value
            case _:
                has_logistics_object = None

        triggered_by: Optional[URIRef]
        match graph.value(subject, API.isTriggeredBy):
            case URIRef(triggered_by_value):
                triggered_by = triggered_by_value
            case _:
                triggered_by = None

        changed_properties: Set[URIRef] = set()
        for o in graph.objects(subject, API.hasChangedProperty):
            match o:
                case URIRef(changed_property_value):
                    changed_properties.add(changed_property_value)
                case _:
                    continue

        return cls(
            # iri=iri,
            event_type=event_type,
            has_logistics_object_type=has_logistics_object_type,
            has_logistics_object=has_logistics_object,
            triggered_by=triggered_by,
            changed_properties=changed_properties,
        )

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        return g
