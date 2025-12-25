from typing import Optional, Self, Set, override

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType

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
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
