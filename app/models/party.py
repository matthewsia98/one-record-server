from typing import Self, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.common import IRI, Graphable
from app.models.logistics_agent import LogisticsAgent


class Party(BaseModel, Graphable):
    party_details: LogisticsAgent
    party_role: IRI

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
