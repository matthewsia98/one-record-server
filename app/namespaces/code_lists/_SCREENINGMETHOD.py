from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SCREENINGMETHOD(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:42.907095
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#")

    _fail = True

    AOM: URIRef  # Subjected to Any Other Means
    CMD: URIRef  # Cargo Metal Detection
    EDD: URIRef  # Explosive Detection Dogs
    EDS: URIRef  # Explosive Detection System
    ETD: URIRef  # Explosives Trace Detection Equipment - Particles or Vapor
    PHS: URIRef  # Physical Inspection and/or Hand Search
    VCK: URIRef  # Visualcheck
    XRY: URIRef  # X-ray Equipment
