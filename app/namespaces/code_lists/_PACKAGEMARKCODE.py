from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PACKAGEMARKCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:14.089102
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/PackageMarkCode#")

    _fail = True

    SSCC_18: URIRef  # Serial Shipping Container Code-18 / EAN-18
    UPC: URIRef  # Universal Product Code
