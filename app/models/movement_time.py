from datetime import datetime
from typing import Optional, Self, override

from pydantic import BaseModel, field_validator
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.namespaces._CARGO import CARGO


class MovementTime(BaseModel, Graphable):
    movement_time_type: IRI
    movement_timestamp: datetime

    @field_validator("movement_time_type")
    def check_movement_time_type(cls, v: IRI) -> IRI:
        allowed = {
            IRI(str(CARGO.ACTUAL)),
            IRI(str(CARGO.ESTIMATED)),
            IRI(str(CARGO.SCHEDULED)),
        }

        if str(v) not in allowed:
            raise ValueError(
                f"movement_time_type must be one of {[str(x) for x in allowed]}"
            )

        return v

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
