from __future__ import annotations

from typing import Optional, Self, Set, override

import orjson
import rdflib
from pydantic import BaseModel, Field, SerializationInfo, model_serializer
from pyld import jsonld
from rdflib import RDF, XSD, Graph, Literal, URIRef
from rdflib.graph import _SubjectType

from app.models.common import IRI, Graphable
from app.namespaces._API import API
from app.namespaces._CARGO import CARGO


class ServerInformation(BaseModel, Graphable):
    has_data_holder: IRI
    has_server_endpoint: IRI
    has_supported_api_version: Set[str] = Field(default_factory=set)
    has_supported_content_type: Set[str] = Field(default_factory=set)
    # has_supported_encoding: Set[str] = Field(default_factory=set)
    has_supported_language: Set[str] = Field(default_factory=set)
    has_supported_ontology: Set[IRI] = Field(default_factory=set)
    # has_supported_ontology_version: Set[IRI] = Field(default_factory=set)

    @override
    def to_graph(self) -> Graph:
        g = Graph()

        subject = URIRef(str(self.has_server_endpoint))
        g.add((subject, rdflib.RDF.type, API.ServerInformation))

        data_holder = URIRef(str(self.has_data_holder))
        g.add((subject, API.hasDataHolder, data_holder))
        g.add((data_holder, rdflib.RDF.type, CARGO.Company))

        g.add(
            (
                subject,
                API.hasServerEndpoint,
                Literal(
                    str(self.has_server_endpoint),
                    datatype=XSD.anyURI,
                ),
            )
        )

        for api_version in self.has_supported_api_version:
            g.add(
                (
                    subject,
                    API.hasSupportedApiVersion,
                    Literal(api_version, datatype=XSD.string),
                )
            )

        for content_type in self.has_supported_content_type:
            g.add(
                (
                    subject,
                    API.hasSupportedContentType,
                    Literal(content_type, datatype=XSD.string),
                )
            )

        for language in self.has_supported_language:
            g.add(
                (
                    subject,
                    API.hasSupportedLanguage,
                    Literal(language, datatype=XSD.string),
                )
            )

        for ontology in self.has_supported_ontology:
            g.add(
                (
                    subject,
                    API.hasSupportedOntology,
                    Literal(ontology, datatype=XSD.anyURI),
                )
            )

        return g

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        if subject is None:
            subject = next(graph.subjects(RDF.type, API.ServerInformation))

        has_data_holder: IRI
        match graph.value(subject, API.hasDataHolder):
            case URIRef(has_data_holder_value):
                has_data_holder = IRI(str(has_data_holder_value))
            case _:
                raise ValueError("ServerInformation is missing hasDataHolder")

        has_server_endpoint: IRI
        match graph.value(subject, API.hasServerEndpoint):
            case Literal(has_server_endpoint_value, datatype=XSD.anyURI):
                has_server_endpoint = IRI(str(has_server_endpoint_value))
            case _:
                raise ValueError("ServerInformation is missing hasServerEndpoint")

        return cls(
            has_data_holder=has_data_holder,
            has_server_endpoint=has_server_endpoint,
        )

    @model_serializer(mode="plain")
    def serialize_model(self, info: SerializationInfo):
        if info.context is not None:
            format = info.context.get("format", "json-ld")
        else:
            format = "json-ld"
        # content_type = rdflib.util.FORMAT_MIMETYPE_MAP.get(format)[0]

        g = self.to_graph()

        serialized = g.serialize(
            format=format,
            context={
                "cargo": CARGO._NS,
                "api": API._NS,
                "xsd": XSD._NS,
            },
        )

        if format == "json-ld":
            SERVER_INFORMATION_FRAME = {
                "@context": {
                    "api": API._NS,
                    "cargo": CARGO._NS,
                    "xsd": XSD._NS,
                    # str(API.hasServerEndpoint): {
                    #     "@type": "xsd:anyURI",
                    # },
                    # str(API.hasSupportedOntology): {
                    #     "@type": "xsd:anyURI",
                    #     # "@container": "@set",
                    # },
                    # str(API.hasSupportedApiVersion): {
                    #     "@container": "@set",
                    # },
                    # str(API.hasSupportedContentType): {
                    #     "@container": "@set",
                    # },
                    # str(API.hasSupportedLanguage): {
                    #     "@container": "@set",
                    # },
                },
                "@type": str(API.ServerInformation),
                "@embed": "@always",
            }

            framed = jsonld.frame(
                orjson.loads(serialized),
                SERVER_INFORMATION_FRAME,
            )

            compacted = jsonld.compact(
                framed,
                SERVER_INFORMATION_FRAME["@context"],
            )

            return orjson.dumps(compacted)
        else:
            return serialized
