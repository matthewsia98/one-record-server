from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PARTICIPANTIDENTIFIER(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:17.100974
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#")

    _fail = True

    AGT: URIRef  # Agent
    AIR: URIRef  # Airline
    APT: URIRef  # Airport Authority
    BRK: URIRef  # Broker
    CAG: URIRef  # Commissionable Agent
    CNE: URIRef  # Consignee
    CTM: URIRef  # Customs
    DCL: URIRef  # Declarant
    DEC: URIRef  # Deconsolidator
    FFW: URIRef  # Freight Forwarder
    GHA: URIRef  # Ground Handling Agent
    NFY: URIRef  # Notify
    PTT: URIRef  # Post Office
    SHP: URIRef  # Shipper
    TRK: URIRef  # Trucker
