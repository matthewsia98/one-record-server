from __future__ import annotations

from typing import Self, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.common import IRI, Graphable


class LogisticsObject(BaseModel, Graphable):
    iri: IRI
    graph: Graph

    model_config = {"arbitrary_types_allowed": True}

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        subject = next(graph.subjects(), None)
        if subject is None:
            raise ValueError("No subject found in the graph")

        iri = IRI(str(subject))

        return cls(
            iri=iri,
            graph=graph,
        )

    @override
    def to_graph(self) -> Graph:
        return self.graph
