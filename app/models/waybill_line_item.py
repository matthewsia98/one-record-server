from typing import Optional, Self, Set, override

from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.models.line_item_package import LineItemPackage


class WaybillLineItem(Graphable):
    line_item_number: int
    line_item_packages: Set[LineItemPackage]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
