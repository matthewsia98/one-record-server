from typing import Optional, Self, override

from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.models.logistics_activity import LogisticsActivity


class ActivitySequence(Graphable):
    activity: LogisticsActivity
    sequence_number: str

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(
        cls,
        graph: Graph,
        subject: Optional[_SubjectType] = None,
    ) -> Self:
        raise NotImplementedError()
