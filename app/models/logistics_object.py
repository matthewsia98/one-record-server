from __future__ import annotations

from typing import Optional, Self, override

from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable


class LogisticsObject(Graphable):
    subject: _SubjectType
    graph: Graph

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects())

        return cls(
            subject=subject,
            graph=graph,
        )

    @override
    def to_graph(self) -> Graph:
        return self.graph
