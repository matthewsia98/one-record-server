from typing import Optional, Self, Set, override

from pydantic import BaseModel, field_validator
from rdflib import Graph
from rdflib.graph import _SubjectType

from app.models.booking import Booking
from app.models.common import IRI, Graphable
from app.models.location import Location
from app.models.shipment import Shipment
from app.models.waybill_line_item import WaybillLineItem
from app.namespaces._CARGO import CARGO


class Waybill(BaseModel, Graphable):
    referred_booking_option: Booking
    shipment: Shipment
    departure_location: Location
    arrival_location: Location
    waybill_type: IRI
    waybill_line_items: Set[WaybillLineItem]
    waybill_number: str
    waybill_prefix: str

    @field_validator("waybill_type")
    def check_waybill_type(cls, v: IRI) -> IRI:
        allowed_waybill_types = {
            IRI(str(CARGO.DIRECT)),
            IRI(str(CARGO.HOUSE)),
            IRI(str(CARGO.MASTER)),
        }

        if v not in allowed_waybill_types:
            raise ValueError(
                f"status must be one of {[str(x) for x in allowed_waybill_types]}"
            )

        return v

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
