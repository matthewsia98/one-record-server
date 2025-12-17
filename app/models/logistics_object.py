from pydantic import BaseModel
from rdflib import Graph

from app.models.common import IRI


class LogisticsObject(BaseModel):
    iri: IRI
    graph: Graph

    model_config = {"arbitrary_types_allowed": True}
