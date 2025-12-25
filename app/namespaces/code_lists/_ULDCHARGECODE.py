from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ULDCHARGECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:30.443859
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#")

    _fail = True

    A: URIRef  # Pivot Rate per kilogram
    B: URIRef  # First Minimum Charge — minimum weight
    C: URIRef  # First over pivot rate per kilogram
    D: URIRef  # Second Minimum Charge — minimum weight
    E: URIRef  # Second over pivot rate per kilogram
    F: URIRef  # Third Minimum Charge — minimum weight
    G: URIRef  # Third over pivot rate per kilogram
    H: URIRef  # Flat Charge — (without weight or with minimum weight)
    I: URIRef  # Flat Charge — maximum weight
