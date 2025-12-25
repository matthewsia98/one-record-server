from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ULDLOADINGINDICATOR(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:33.604410
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#")

    _fail = True

    L: URIRef  # ULD Height below 160 centimetres
    M: URIRef  # Main Deck Loading only
    N: URIRef  # Nose Door Loading only
    R: URIRef  # ULD Height above 244 centimetres
    U: URIRef  # ULD Height between 160 centimetres and 244 centimetres
