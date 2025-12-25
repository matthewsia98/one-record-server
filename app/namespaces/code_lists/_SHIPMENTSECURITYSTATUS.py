from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SHIPMENTSECURITYSTATUS(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:25.810035
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ShipmentSecurityStatus#")

    _fail = True

    NCR: URIRef  # Screened
    SCR: URIRef  # Not Screened
