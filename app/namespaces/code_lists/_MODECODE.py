from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class MODECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:11.716433
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ModeCode#")

    _fail = True

    AIR_TRANSPORT: URIRef  # Indicates the transport mode to be Air Transport (4)
    FIXED_TRANSPORT_INSTALLATION: URIRef  # Indicates that the transport mode is a Fixed Transport Installation (7)
    INLAND_WATER_TRANSPORT: (
        URIRef  # Indicates that the transport mode to be Inland Water Transport (8)
    )
    MAIL: URIRef  # Indicates the transport mode to be Mail (5)
    MARITIME_TRANSPORT: (
        URIRef  # Indicates the transport mode to be Maritime Transport (1)
    )
    MULTIMODAL_TRANSPORT: URIRef  # Indicates a Multimodal Transport (6)
    RAIL_TRANSPORT: URIRef  # Indicates the transport mode to be Rail Transport (2)
    ROAD_TRANSPORT: URIRef  # Indicates the transport mode to be Road Transport (3)
    TRANSPORT_MODE_NOT_APPLICABLE: (
        URIRef  # Indicates that no transport mode is applicable (9)
    )
    TRANSPORT_MODE_NOT_SPECIFIED: (
        URIRef  # Indicates that the Transport Mode is not specified (0)
    )
