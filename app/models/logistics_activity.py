from typing import Optional, Self, override

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable


class LogisticsActivity(BaseModel, Graphable):
    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
