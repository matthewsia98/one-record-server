from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class AWBUSEINDICATOR(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 02:55:56.926957
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#")

    _fail = True

    R: URIRef  # Revenue AWB
    S: URIRef  # Service AWB
    V: URIRef  # Void AWB
