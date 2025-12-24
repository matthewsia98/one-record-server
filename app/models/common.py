from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Annotated, Self

from fastapi import Depends
from pydantic import AnyUrl, UrlConstraints
from rdflib import Graph

from app.dependencies.graph import parse_graph

IRI = Annotated[AnyUrl, UrlConstraints()]


class Graphable(ABC):
    @abstractmethod
    def to_graph(self) -> Graph: ...

    @classmethod
    @abstractmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self: ...
