from __future__ import annotations

from typing import Optional, Self, override

from pydantic import BaseModel
from rdflib import Graph, URIRef
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable


class LogisticsObject(BaseModel, Graphable):
    iri: Optional[IRI] = None
    graph: Graph

    model_config = {"arbitrary_types_allowed": True}

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects())

        iri: Optional[IRI]
        match subject:
            case URIRef(iri_value):
                iri = IRI(str(iri_value))
            case _:
                iri = None

        return cls(
            iri=iri,
            graph=graph,
        )

    @override
    def to_graph(self) -> Graph:
        return self.graph
