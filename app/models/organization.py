from __future__ import annotations

from typing import Self, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import RDF, BNode, Graph, Literal

from app.dependencies.graph import parse_graph
from app.models.common import Graphable
from app.namespaces._CARGO import CARGO


class Organization(BaseModel, Graphable):
    name: str

    @override
    @classmethod
    def from_graph(cls, g: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        subject = BNode("_data-holder")
        g.add((subject, RDF.type, CARGO.Organization))
        g.add((subject, RDF.type, CARGO.LogisticsObject))
        g.add((subject, CARGO.name, Literal(self.name)))

        return g
