from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class TRANSPORTMEANSSERVICETYPE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:29.667971
    """

    _NS = Namespace(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#"
    )

    _fail = True

    FREIGHTER: URIRef  # Transport leg performed by freighter aircraft
    MIXED_CONFIGURATION_COMBI: (
        URIRef  # Transport leg performed by mixed configuration combi aircraft
    )
    PASSENGER: URIRef  # Transport leg performed by passenger aircraft
    TRUCK: URIRef  # Transport leg performed by truck
