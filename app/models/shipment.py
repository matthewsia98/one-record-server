from typing import Optional, Self, Set, override

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.models.party import Party
from app.models.piece import Piece
from app.models.value import Value


class Shipment(BaseModel, Graphable):
    pieces: Set[Piece]
    total_gross_weight: Value
    involved_parties: Set[Party]
    goods_description: str

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
