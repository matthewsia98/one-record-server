from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SIGNATURETYPECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:27.370996
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#")

    _fail = True

    DETENTION: URIRef  # Detention
    FUMIGATION: URIRef  # Fumigation
    INSPECTION: URIRef  # Inspection
    SECURITY: URIRef  # Security
