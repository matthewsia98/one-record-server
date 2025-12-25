from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class GOODSTYPECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:09.373934
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#")

    _fail = True

    I: URIRef  # Species included in Appendix I of CITES
    II: URIRef  # Species included in Appendix II of CITES
    III: URIRef  # Species included in Appendix III of CITES
