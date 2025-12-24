from typing import Self, Set, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
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
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
