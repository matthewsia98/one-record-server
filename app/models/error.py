from __future__ import annotations

from typing import Optional, Self, Set, override

from pydantic import Field
from rdflib import RDF, XSD, BNode, Graph, Literal, URIRef
from rdflib.graph import _SubjectType

from app.models.common import Graphable
from app.namespaces._API import API


class ErrorDetail(Graphable):
    # subject: _SubjectType
    code: str
    message: Optional[str] = None
    property: Optional[URIRef] = None
    resource: Optional[URIRef] = None

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        node = BNode()
        g.add((node, RDF.type, API.ErrorDetail))
        g.add((node, API.hasProperty, Literal(self.property, datatype=XSD.anyURI)))

        return g

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()


class Error(Graphable):
    # subject: _SubjectType
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
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()

    @classmethod
    def create_error(
        cls,
        # subject: _SubjectType,
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
        # subject: _SubjectType,
        title: str,
        # detail_subject: _SubjectType,
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
