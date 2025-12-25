from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PACKAGINGDANGERLEVELCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:16.312081
    """

    _NS = Namespace(
        "https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#"
    )

    _fail = True

    I: URIRef  # High danger
    II: URIRef  # Medium danger
    III: URIRef  # Low danger
