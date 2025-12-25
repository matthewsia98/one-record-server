from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Annotated, Optional, Self

from pydantic import AnyUrl, UrlConstraints
from rdflib import Graph
from rdflib.graph import _SubjectType

IRI = Annotated[AnyUrl, UrlConstraints()]


class Graphable(ABC):
    @abstractmethod
    def to_graph(self) -> Graph: ...

    @classmethod
    @abstractmethod
    def from_graph(
        cls,
        graph: Graph,
        subject: Optional[_SubjectType] = None,
    ) -> Self: ...
