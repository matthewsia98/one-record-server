from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class REGULATEDENTITYCATEGORYCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:41.309682
    """

    _NS = Namespace(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#"
    )

    _fail = True

    AO: URIRef  # Aircraft Operator
    KC: URIRef  # Known Consignor (consignor for both passenger and all cargo aircraft only)
    RA: URIRef  # Regulated Agent
    RC: URIRef  # Regulated Carrier
