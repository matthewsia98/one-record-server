from typing import Optional, Self, override

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable


class CodeListElement(BaseModel, Graphable):
    code: str
    code_description: str
    code_level: int
    code_list_name: str
    code_list_reference: str
    code_list_version: str

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
