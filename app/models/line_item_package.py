from typing import Self, Set, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.common import Graphable
from app.models.piece import Piece
from app.models.value import Value


class LineItemPackage(BaseModel, Graphable):
    package_gross_weight: Value
    package_volume: Value
    piece_references: Set[Piece]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
