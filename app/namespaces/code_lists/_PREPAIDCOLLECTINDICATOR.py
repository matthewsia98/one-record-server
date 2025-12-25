from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PREPAIDCOLLECTINDICATOR(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:17.953310
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#")

    _fail = True

    C: URIRef  # Collect Indicator
    P: URIRef  # Prepaid Indicator
