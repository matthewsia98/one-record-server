from __future__ import annotations

from datetime import datetime, timezone
from typing import ClassVar, Self, Set, override

import aiohttp
import orjson
from devtools import debug
from fastapi import APIRouter, Depends, Response, status
from pydantic import BaseModel, Field, field_validator
from pyld import jsonld
from rdflib import RDF, XSD, BNode, Graph, Literal, URIRef

from app.dependencies.graph import parse_graph
from app.dependencies.http_client import get_http_client
from app.models.common import IRI, Graphable
from app.models.error import Error
from app.namespaces._API import API
from app.namespaces._CARGO import CARGO


class Assessment(BaseModel, Graphable):
    STATUS_DICT: ClassVar = {
        "ASC": "Assessment Completion",
        "RFI": "Request for information",
        "RFS": "Request for screening",
        "DNL": "Do Not Load",
    }

    target: IRI
    status: str
    errors: Set[str] = Field(default_factory=set)

    @field_validator("status")
    def check_status(cls, v: str) -> str:
        if v not in Assessment.STATUS_DICT:
            raise ValueError(
                f"status must be one of {list(Assessment.STATUS_DICT.keys())}"
            )
        return v

    @override
    @classmethod
    def from_graph(cls, graph: Graph = Depends(parse_graph)) -> Self:
        raise NotImplementedError()

    def to_logistics_event_graph(self) -> Graph:
        g = Graph()

        node = BNode()

        g.add((node, RDF.type, CARGO.LogisticsEvent))

        g.add(
            (
                node,
                CARGO.creationDate,
                Literal(
                    datetime.now(tz=timezone.utc),
                    datatype=XSD.dateTime,
                ),
            )
        )

        g.add(
            (
                node,
                CARGO.eventDate,
                Literal(
                    datetime.now(tz=timezone.utc),
                    datatype=XSD.dateTime,
                ),
            )
        )

        event_code = BNode()
        g.add((node, CARGO.eventCode, event_code))
        g.add((event_code, RDF.type, CARGO.CodeListElement))
        g.add((event_code, CARGO.code, Literal(self.status)))
        g.add(
            (
                event_code,
                CARGO.codeListName,
                Literal(Assessment.STATUS_DICT[self.status]),
            )
        )

        g.add((node, CARGO.eventName, Literal(Assessment.STATUS_DICT[self.status])))

        event_time_type = URIRef(CARGO.ACTUAL)
        g.add((node, CARGO.eventTimeType, event_time_type))
        g.add((event_time_type, RDF.type, CARGO.EventTimeType))

        g.add((node, CARGO.partialEventIndicator, Literal(False, datatype=XSD.boolean)))

        return g

    def to_verification_graph(self) -> Graph:
        g = Graph()

        node = BNode()

        g.add((node, RDF.type, CARGO.Verification))

        g.add((node, API.hasLogisticsObject, URIRef(str(self.target))))

        for error in self.errors:
            error_graph = Error(title=error).to_graph()
            g += error_graph
            error_node = next(error_graph.subjects())
            g.add((node, CARGO.hasError, error_node))

        g.add((node, API.hasRevision, Literal(1, datatype=XSD.positiveInteger)))

        return g

    @override
    def to_graph(self) -> Graph:
        return self.to_logistics_event_graph()


router = APIRouter()


@router.post(
    "/internal/assessment",
    tags=["internal"],
    status_code=status.HTTP_201_CREATED,
    response_class=Response,
)
async def create_assessment(
    assessment: Assessment,
    http_client: aiohttp.ClientSession = Depends(get_http_client),
):
    debug(assessment)

    g = assessment.to_graph()
    debug(g.serialize(format="json-ld"))

    serialized = g.serialize(format="json-ld")

    FRAME = {
        "@context": {
            "cargo": str(CARGO._NS),
        },
        "@type": str(CARGO.LogisticsEvent),
        "@embed": "@always",
    }
    framed = jsonld.frame(orjson.loads(serialized), FRAME)
    compacted = jsonld.compact(framed, FRAME)

    debug(compacted)

    try:
        url = "/".join(
            [
                str(assessment.target).rstrip("/"),
                "logistics-events",
            ]
        )
        debug(url)
        async with http_client.post(
            url,
            json=compacted,
            headers={
                "Accept": "application/ld+json",
                "Content-Type": "application/ld+json",
            },
        ) as response:
            debug(response.status)
    except Exception as e:
        debug(e)

    return Response(
        status_code=status.HTTP_201_CREATED,
        content=orjson.dumps(compacted),
        media_type="application/ld+json",
    )
