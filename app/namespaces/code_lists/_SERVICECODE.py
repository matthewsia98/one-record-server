from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SERVICECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:25.041418
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ServiceCode#")

    _fail = True

    A: URIRef  # Airport-to-Airport
    B: URIRef  # Service Shipment
    C: URIRef  # Company Material
    D: URIRef  # Door-to-Door Service
    E: URIRef  # Airport-to-Door
    F: URIRef  # Flight Specific
    G: URIRef  # Door-to-Airport
    H: URIRef  # Company Mail
    I: URIRef  # Diplomatic Mail
    J: URIRef  # Priority Service
    P: URIRef  # Small Package Service
    S: URIRef  # Substitute Truck
    T: URIRef  # Charter
    X: URIRef  # Express Shipments
