from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ULDCONDITIONCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 02:56:13.522634
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#")

    _fail = True

    DAM: URIRef  # Damaged But Still Serviceable
    SER: URIRef  # Serviceable
