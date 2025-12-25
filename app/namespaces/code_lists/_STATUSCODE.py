from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class STATUSCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:28.101288
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/StatusCode#")

    _fail = True

    ARR: URIRef  # The consignment has arrived on a scheduled flight at this location
    AWD: URIRef  # The arrival documentation has been physically delivered to the consignee or the consignee’s agent on this date at this location
    AWR: URIRef  # The arrival documentation has been physically received from a scheduled flight at this location
    BKD: URIRef  # The consignment has been booked for transport between these locations on this scheduled date and this flight
    CCD: URIRef  # The consignment has been cleared by the Customs authorities on this date at this location
    CRC: URIRef  # The consignment has been reported to the Customs authorities on this date at this location
    DDL: URIRef  # The consignment has been physically delivered to the consignee’s door on this date at this location
    DEP: URIRef  # The consignment has physically departed this location on this scheduled date and flight for transport to the arrival location
    DIS_DFLD: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Definitely Loaded
    DIS_FDAV: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mail Document
    DIS_FDAW: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Air Waybill
    DIS_FDCA: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Cargo
    DIS_FDMB: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mailbag
    DIS_MSAV: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mail Document
    DIS_MSAW: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Air Waybill
    DIS_MSCA: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Cargo
    DIS_MSMB: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mailbag
    DIS_OFLD: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Offloaded
    DIS_OVCD: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Overcarried
    DIS_SSPD: URIRef  # An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Shortshipped
    DLV: URIRef  # The consignment has been physically delivered to the consignee or the Consignee’s agent on this date at this location
    DOC: URIRef  # Documents Received by Handling Party
    DPU: URIRef  # The consignment has been physically picked up from the shipper’s door on this date at this location
    FIW: URIRef  # Freight Into Warehouse Control
    FOH: URIRef  # The consignment is on hand on this date at this location pending “ready for carriage” determination
    FOW: URIRef  # Freight Out of Warehouse Control
    MAN: URIRef  # The consignment has been manifested for this flight on this scheduled date for transport between these locations
    NFD: URIRef  # The consignee or the consignee’s agent has been notified, on this date at this location, of the arrival of the consignment
    OCI: URIRef  # Other Customs, Security and Regulatory Control Information
    OSI: URIRef  # Other Service Information
    PRE: URIRef  # The consignment has been prepared for loading on this flight for transport between these locations on this scheduled date
    RCF: URIRef  # The consignment has been physically received from a given flight or surface transport of the given airline
    RCS: URIRef  # The consignment has been physically received from the shipper or the shipper’s agent and is considered by the carrier as ready for carriage on this date at this location
    RCT: URIRef  # The consignment has been physically received from this carrier on this date at this location
    TFD: URIRef  # The consignment has been physically transferred to this carrier on this date at this location
    TGC: URIRef  # The consignment has been transferred to Customs/Government control
    TRM: URIRef  # The consignment has been manifested and/or will be physically transferred to this carrier at this location
