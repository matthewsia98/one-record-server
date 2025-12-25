from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class CHARGEIDENTIFIER(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:24.953020
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#")

    _fail = True

    CN: URIRef  # CASS Net Amount
    CO: URIRef  # Commission
    CT: URIRef  # Charge Summary Total
    IN: URIRef  # Insurance
    NI: URIRef  # CASS Invoice Amount
    OA: URIRef  # Total Other Charges Due Agent
    OC: URIRef  # Total Other Charges Due Carrier
    SI: URIRef  # Sales Incentive
    TX: URIRef  # Taxes
    VC: URIRef  # Valuation Charge
    WT: URIRef  # Total Weight Charge
