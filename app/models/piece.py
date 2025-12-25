from typing import Optional, Self, Set, override

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.models.value import Value


class Piece(BaseModel, Graphable):
    goods_description: str
    gross_weight: Value
    special_handling_codes: Set[IRI]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
