from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class GOODSTYPEEXTENSIONCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:30.926505
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#")

    _fail = True

    A: URIRef  # Artificially propagated plant
    C: URIRef  # Bred in captivity
    D: URIRef  # Captive-bred animal or artificially propagated plant
    F: URIRef  # Born in captivity
    I: URIRef  # Confiscated or seized
    O: URIRef  # Pre-Convention
    R: URIRef  # Ranched animal
    U: URIRef  # Unknown
    W: URIRef  # Wild
    X: URIRef  # Marine environment
