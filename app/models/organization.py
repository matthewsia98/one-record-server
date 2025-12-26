from __future__ import annotations

from typing import Optional, Self, override

from rdflib import RDF, BNode, Graph, Literal
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.namespaces._CARGO import CARGO


class Organization(Graphable):
    name: str

    @override
    @classmethod
    def from_graph(cls, g: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        subject = BNode("_data-holder")
        g.add((subject, RDF.type, CARGO.Organization))
        g.add((subject, RDF.type, CARGO.LogisticsObject))
        g.add((subject, CARGO.name, Literal(self.name)))

        return g
