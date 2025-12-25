from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ENTITLEMENTCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:07.789216
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/EntitlementCode#")

    _fail = True

    A: URIRef  # Other Charges due Agent
    C: URIRef  # Other Charges due Carrier
