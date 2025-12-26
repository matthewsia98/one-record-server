from typing import Annotated, Optional, Self, override

from pydantic import PlainValidator
from rdflib import Graph, URIRef
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.validators.participant_identifier_validator import (
    ParticipantIdentifierValidator,
)


class Party(Graphable):
    # party_details: LogisticsAgent
    party_role: Annotated[
        URIRef, PlainValidator(ParticipantIdentifierValidator.validate)
    ]

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
