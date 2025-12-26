from typing import Annotated, Optional, Self, Set, override

from pydantic import PlainValidator
from rdflib import Graph, URIRef
from rdflib.graph import _SubjectType

from app.models.booking import Booking
from app.models.location import Location
from app.models.logistics_object import LogisticsObject
from app.models.shipment import Shipment
from app.models.waybill_line_item import WaybillLineItem
from app.validators.waybill_type_validator import WaybillTypeValidator


class Waybill(LogisticsObject):
    referred_booking_option: Booking
    shipment: Shipment
    departure_location: Location
    arrival_location: Location
    waybill_type: Annotated[URIRef, PlainValidator(WaybillTypeValidator.validate)]
    waybill_line_items: Set[WaybillLineItem]
    waybill_number: str
    waybill_prefix: str

    @override
    def to_graph(self) -> Graph:
        raise NotImplementedError()

    @override
    @classmethod
    def from_graph(cls, graph: Graph, subject: Optional[_SubjectType] = None) -> Self:
        raise NotImplementedError()
