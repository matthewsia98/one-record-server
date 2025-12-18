from typing import override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.common import IRI


class LogisticsObject(BaseModel):
    iri: IRI
    graph: Graph

    model_config = {"arbitrary_types_allowed": True}

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> LogisticsObject:
        subject = next(graph.subjects(), None)
        if subject is None:
            raise ValueError("No subject found in the graph")

        iri = IRI(str(subject))

        return LogisticsObject(
            iri=iri,
            graph=graph,
        )

    @override
    def to_graph(self) -> Graph:
        return self.graph
