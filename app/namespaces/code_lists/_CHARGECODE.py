from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class CHARGECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:05.284308
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/ChargeCode#")

    _fail = True

    CA: URIRef  # Partial Collect Credit — Partial Prepaid Cash
    CB: URIRef  # Partial Collect Credit — Partial Prepaid Credit
    CC: URIRef  # All Charges Collect
    CE: URIRef  # Partial Collect Credit Card — Partial Prepaid Cash
    CG: URIRef  # All Charges Collect by GBL
    CH: URIRef  # Partial Collect Credit Card — Partial Prepaid Credit
    CM: URIRef  # Destination Collect by MCO
    CP: URIRef  # Destination Collect Cash
    CX: URIRef  # Destination Collect Credit
    CZ: URIRef  # All Charges Collect by Credit Card
    NC: URIRef  # No Charge
    NG: URIRef  # No Weight Charge — Other Charges Prepaid by GBL
    NP: URIRef  # No Weight Charge — Other Charges Prepaid Cash
    NT: URIRef  # No Weight Charge — Other Charges Collect
    NX: URIRef  # No Weight Charge — Other Charges Prepaid Credit
    NZ: URIRef  # No Weight Charge — Other Charges Prepaid by Credit Card
    PC: URIRef  # Partial Prepaid Cash — Partial Collect Cash
    PD: URIRef  # Partial Prepaid Credit — Partial Collect Cash
    PE: URIRef  # Partial Prepaid Credit Card — Partial Collect Cash
    PF: URIRef  # Partial Prepaid Credit Card — Partial Collect Credit Card
    PG: URIRef  # All Charges Prepaid by GBL
    PH: URIRef  # Partial Prepaid Credit Card — Partial Collect Credit
    PP: URIRef  # All Charges Prepaid Cash
    PX: URIRef  # All Charges Prepaid Credit
    PZ: URIRef  # All Charges Prepaid by Credit Card
