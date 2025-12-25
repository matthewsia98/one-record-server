from typing import Optional, Self, override

from pydantic import BaseModel
from rdflib import RDF, Graph, Literal, URIRef
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.namespaces._CARGO import CARGO


class Value(BaseModel, Graphable):
    unit: IRI
    numerical_value: float

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects(RDF.type, CARGO.Value))

        unit: IRI
        match graph.value(subject, CARGO.unit):
            case URIRef(iri_value):
                unit = IRI(str(iri_value))

        numerical_value: float
        match graph.value(subject, CARGO.numericalValue):
            case Literal(num_value):
                numerical_value = float(num_value)

        return cls(
            unit=unit,
            numerical_value=numerical_value,
        )
