from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class RADIOACTIVEMATERIALCLASSIFICATION(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:38.935147
    """

    _NS = Namespace(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#"
    )

    _fail = True

    LOW_DISPERSIBLE: URIRef  # Low Dispersible
    PHYSICAL_CHEMICAL_FORM: URIRef  # Physical Chemical Form
    SPECIAL_FORM: URIRef  # Special Form
