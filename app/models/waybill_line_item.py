from typing import Self, Set, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.common import Graphable
from app.models.line_item_package import LineItemPackage


class WaybillLineItem(BaseModel, Graphable):
    line_item_number: int
    line_item_packages: Set[LineItemPackage]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
