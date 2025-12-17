from abc import ABC, abstractmethod
from typing import Annotated

from pydantic import AnyUrl, UrlConstraints
from rdflib import Graph

IRI = Annotated[AnyUrl, UrlConstraints()]


class Graphable(ABC):
    @abstractmethod
    def to_graph(self) -> Graph: ...
