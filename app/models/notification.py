from typing import Optional, Set

from fastapi import Depends
from pydantic import BaseModel, Field
from rdflib import RDF, Graph, Literal, URIRef

from app.dependencies.graph import parse_graph
from app.models.common import IRI
from app.models.logistics_object import LogisticsObject
from app.namespaces._API import API


class NotificationMessage(BaseModel):
    notification: Notification
    logistics_object: Optional[LogisticsObject] = None


class Notification(BaseModel):
    iri: IRI
    event_type: IRI
    has_logistics_object_type: Optional[str] = None
    has_logistics_object: Optional[IRI] = None
    triggered_by: Optional[IRI] = None
    changed_properties: Set[IRI] = Field(default_factory=set)

    @classmethod
    async def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Notification:
        """
        Construct a Notification instance from an RDF graph.
        Assumes there is exactly one Notification in the graph.
        """
        # Find the subject node of type API.Notification
        subject = next(graph.subjects(RDF.type, API.Notification), None)
        if subject is None:
            raise ValueError("No Notification found in the graph")

        iri = IRI(str(subject))

        match graph.value(subject, API.hasEventType):
            case URIRef(has_event_type_value):
                event_type = IRI(str(has_event_type_value))
            case _:
                raise ValueError("Notification is missing hasEventType")

        has_logistics_object_type: Optional[str]
        match graph.value(subject, API.hasLogisticsObjectType):
            case Literal(has_logistics_object_type_value):
                has_logistics_object_type = str(has_logistics_object_type_value)
            case _:
                has_logistics_object_type = None

        has_logistics_object: Optional[IRI]
        match graph.value(subject, API.hasLogisticsObject):
            case URIRef(has_logistics_object_value):
                has_logistics_object = IRI(str(has_logistics_object_value))
            case _:
                has_logistics_object = None

        triggered_by: Optional[IRI]
        match graph.value(subject, API.isTriggeredBy):
            case URIRef(triggered_by_value):
                triggered_by = IRI(str(triggered_by_value))
            case _:
                triggered_by = None

        changed_properties: Set[IRI] = set()
        for o in graph.objects(subject, API.hasChangedProperty):
            match o:
                case URIRef(changed_property_value):
                    changed_properties.add(IRI(str(changed_property_value)))
                case _:
                    continue

        return Notification(
            iri=iri,
            event_type=event_type,
            has_logistics_object_type=has_logistics_object_type,
            has_logistics_object=has_logistics_object,
            triggered_by=triggered_by,
            changed_properties=changed_properties,
        )
