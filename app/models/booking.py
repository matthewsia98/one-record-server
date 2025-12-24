from typing import List, Self, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.activity_sequence import ActivitySequence
from app.models.common import Graphable


class Booking(BaseModel, Graphable):
    activity_sequences: List[ActivitySequence]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
