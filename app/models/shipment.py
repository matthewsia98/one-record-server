from typing import List, Optional, Self, override

from pydantic import BaseModel, Field
from rdflib import RDF, Graph, Literal, Node, URIRef
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.models.party import Party
from app.models.piece import Piece
from app.models.value import Value
from app.namespaces._CARGO import CARGO


class Shipment(BaseModel, Graphable):
    iri: Optional[IRI] = None
    pieces: List[Piece] = Field(default_factory=list)
    total_gross_weight: Optional[Value] = None
    involved_parties: List[Party] = Field(default_factory=list)
    goods_description: Optional[str] = None

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects(RDF.type, CARGO.Shipment))

        iri: Optional[IRI]
        match subject:
            case URIRef():
                iri = IRI(str(subject))
            case _:
                iri = None

        pieces: List[Piece] = []
        for obj in graph.objects(subject, CARGO.pieces):
            match obj:
                case Node():
                    pieces.append(
                        Piece.from_graph(
                            graph,
                            obj,
                        )
                    )

        total_gross_weight: Optional[Value]
        match graph.value(subject, CARGO.totalGrossWeight):
            case Node():
                total_gross_weight = Value.from_graph(
                    graph,
                    graph.value(subject, CARGO.totalGrossWeight),
                )
            case _:
                total_gross_weight = None

        involved_parties: List[Party] = []

        goods_description: Optional[str]
        match graph.value(subject, CARGO.goodsDescription):
            case Literal(goods_description_value):
                goods_description = str(goods_description_value)
            case _:
                goods_description = None

        return cls(
            iri=iri,
            pieces=pieces,
            total_gross_weight=total_gross_weight,
            involved_parties=involved_parties,
            goods_description=goods_description,
        )
