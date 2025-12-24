from typing import Self, override

from fastapi import Depends
from pydantic import BaseModel
from rdflib import Graph

from app.dependencies.graph import parse_graph
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
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()
