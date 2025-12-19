from __future__ import annotations

from typing import Optional, Set, override

from fastapi import Depends
from pydantic import BaseModel, Field
from rdflib import RDF, XSD, BNode, Graph, Literal

from app.dependencies.graph import parse_graph
from app.models.common import IRI, Graphable
from app.namespaces._API import API


class ErrorDetail(BaseModel, Graphable):
    # iri: IRI
    code: str
    message: Optional[str] = None
    property: Optional[IRI] = None
    resource: Optional[IRI] = None

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        node = BNode()
        g.add((node, RDF.type, API.ErrorDetail))
        g.add((node, API.hasProperty, Literal(self.property, datatype=XSD.anyURI)))

        return g

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> ErrorDetail:
        raise NotImplementedError()


class Error(BaseModel, Graphable):
    # iri: IRI
    title: str
    error_detail: Set[ErrorDetail] = Field(default_factory=set)

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        node = BNode()
        g.add((node, RDF.type, API.Error))
        g.add((node, API.hasTitle, Literal(self.title)))

        for detail in self.error_detail:
            detail_graph = detail.to_graph()
            g += detail_graph
            detail_node = next(detail_graph.subjects())
            g.add((node, API.hasErrorDetail, detail_node))

        return g

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Error:
        raise NotImplementedError()

    @classmethod
    def create_error(
        cls,
        # iri: IRI,
        title: str,
        detail: ErrorDetail,
    ) -> Error:
        return Error(
            # iri=iri,
            title=title,
            error_detail=set([detail]),
        )

    @classmethod
    def create_error_with_info(
        cls,
        # iri: IRI,
        title: str,
        # detail_iri: IRI,
        code: str,
        detail_message: str,
    ) -> Error:
        return Error(
            # iri=iri,
            title=title,
            error_detail=set(
                [
                    ErrorDetail(
                        # iri=detail_iri,
                        code=code,
                        message=detail_message,
                    )
                ]
            ),
        )
