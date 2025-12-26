from typing import Optional, Self, Set, override

from pydantic import Field
from rdflib import RDF, XSD, Graph, Literal, Node, URIRef
from rdflib.graph import _SubjectType

from app.models.physical_logistics_object import PhysicalLogisticsObject
from app.models.value import Value
from app.namespaces._CARGO import CARGO


class Piece(PhysicalLogisticsObject):
    subject: _SubjectType
    goods_description: Optional[str] = None
    gross_weight: Optional[Value] = None
    special_handling_codes: Set[URIRef] = Field(default_factory=set)

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects(RDF.type, CARGO.Piece))

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

        special_handling_codes: Set[URIRef] = set()
        for obj in graph.objects(subject, CARGO.specialHandlingCodes):
            match obj:
                case URIRef(iri_value):
                    special_handling_codes.add(iri_value)

        return cls(
            subject=subject,
            graph=graph,
            goods_description=goods_description,
            gross_weight=gross_weight,
            special_handling_codes=special_handling_codes,
        )
