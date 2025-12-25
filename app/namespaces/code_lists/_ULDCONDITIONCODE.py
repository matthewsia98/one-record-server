from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ULDCONDITIONCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:31.229227
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#")

    _fail = True

    DAM: URIRef  # Damaged But Still Serviceable
    SER: URIRef  # Serviceable
