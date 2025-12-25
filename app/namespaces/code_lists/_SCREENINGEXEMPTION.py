from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SCREENINGEXEMPTION(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:22.731251
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#")

    _fail = True

    BIOM: URIRef  # Bio-Medical Samples
    DIPL: URIRef  # Diplomatic Bags or Diplomatic Mail
    LFSM: URIRef  # Life-Saving Materials (Save Human Life)
    MAIL: URIRef  # Mail
    NUCL: URIRef  # Nuclear Material
    SMUS: URIRef  # Small Undersized Shipments
    TRNS: URIRef  # Transfer or Transshipment
