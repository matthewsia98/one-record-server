from typing import Optional, Self, Set, override

from pydantic import BaseModel, Field
from rdflib import RDF, XSD, Graph, Literal, Node, URIRef
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.models.value import Value
from app.namespaces._CARGO import CARGO


class Piece(BaseModel, Graphable):
    iri: Optional[IRI] = None
    goods_description: Optional[str] = None
    gross_weight: Optional[Value] = None
    special_handling_codes: Set[IRI] = Field(default_factory=set)

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects(RDF.type, CARGO.Piece))

        iri: Optional[IRI]
        match subject:
            case URIRef(iri_value):
                iri = IRI(str(iri_value))
            case _:
                iri = None

        goods_description: Optional[str]
        match graph.value(subject, CARGO.goodsDescription):
            case Literal(goods_description_value, datatype=XSD.string):
                goods_description = str(goods_description_value)
            case _:
                goods_description = None

        gross_weight: Optional[Value]
        match graph.value(subject, CARGO.grossWeight):
            case Node():
                gross_weight = Value.from_graph(
                    graph,
                    graph.value(subject, CARGO.grossWeight),
                )
            case _:
                gross_weight = None

        special_handling_codes: Set[IRI] = set()
        for obj in graph.objects(subject, CARGO.specialHandlingCodes):
            match obj:
                case URIRef(iri_value):
                    special_handling_codes.add(IRI(str(iri_value)))

        return cls(
            iri=iri,
            goods_description=goods_description,
            gross_weight=gross_weight,
            special_handling_codes=special_handling_codes,
        )
