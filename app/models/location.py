from typing import Self, Set, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
from app.models.address import Address
from app.models.code_list_element import CodeListElement
from app.models.common import Graphable


class Location(BaseModel, Graphable):
    address: Address
    location_codes: Set[CodeListElement]
    location_name: str
    location_type: str

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
