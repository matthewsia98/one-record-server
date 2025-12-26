from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Self

from pydantic import BaseModel
from rdflib import Graph
from rdflib.graph import _SubjectType


class Graphable(BaseModel, ABC):
    model_config = {
        "arbitrary_types_allowed": True,
    }

    @abstractmethod
    def to_graph(self) -> Graph: ...

    @classmethod
    @abstractmethod
    def from_graph(
        cls,
        graph: Graph,
        subject: Optional[_SubjectType] = None,
    ) -> Self: ...
