from typing import Optional, Self, Set, override

from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.models.piece import Piece
from app.models.value import Value


class LineItemPackage(Graphable):
    package_gross_weight: Value
    package_volume: Value
    piece_references: Set[Piece]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
