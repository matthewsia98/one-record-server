from datetime import datetime
from typing import Annotated, Optional, Self, override

from pydantic import PlainValidator
from rdflib import Graph, URIRef
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.validators.movement_time_type_validator import MovementTimeTypeValidator


class MovementTime(Graphable):
    movement_time_type: Annotated[
        URIRef, PlainValidator(MovementTimeTypeValidator.validate)
    ]
    movement_timestamp: datetime

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
