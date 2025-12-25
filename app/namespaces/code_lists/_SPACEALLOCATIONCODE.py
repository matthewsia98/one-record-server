from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SPACEALLOCATIONCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:47.723909
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#")

    _fail = True

    CA: URIRef  # Action code - Selling Space Allocation Against Allotment
    CN: URIRef  # Advice Code - Cancellation Noted
    HK: URIRef  # Status Code - Holding Confirmed
    HL: URIRef  # Status Code - Holding Wait List
    HN: URIRef  # Status Code - Have Requested Space Allocation
    KK: URIRef  # Advice Code - Confirming
    LL: URIRef  # Advice Code - Wait List
    NA: URIRef  # Action code - Requesting Space Allocation, if Not Available Will Accept  Alternative
    NL: URIRef  # Action Code - Requesting Space Allocation, for Wait List
    NN: URIRef  # Action Code - Requesting Space Allocation, Will Not Accept Alternative
    SS: URIRef  # Action Code - Reporting Sale
    UN: URIRef  # Advice Code - Unable, Flight Does Not Operate
    UU: URIRef  # Advice Code - Unable
    XX: URIRef  # Action Code - Cancel Any Previous Space Allocation
