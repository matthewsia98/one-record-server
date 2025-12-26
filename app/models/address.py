from typing import List, Optional, Self, override

from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.code_list_element import CodeListElement
from app.models.common import Graphable


class Address(Graphable):
    address_code: CodeListElement
    city_code: CodeListElement
    country: CodeListElement
    postal_code: CodeListElement
    region_code: CodeListElement
    city_name: str
    post_office_box: str
    textual_post_code: str
    street_address_lines: List[str]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
