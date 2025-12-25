from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class RATECLASSCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:39.724789
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/RateClassCode#")

    _fail = True

    B: URIRef  # Basic Charge
    C: URIRef  # Specific Commodity Rate
    E: URIRef  # Unit Load Device Additional Rate
    K: URIRef  # Rate per Kilogram
    M: URIRef  # Minimum Charge
    N: URIRef  # Normal Rate
    P: URIRef  # International Priority Service Rate
    Q: URIRef  # Quantity Rate
    R: URIRef  # Class Rate Reduction
    S: URIRef  # Class Rate Surcharge
    U: URIRef  # Unit Load Device Basic Charge or Rate
    W: URIRef  # Weight Increase
    X: URIRef  # Unit Load Device Additional Information
    Y: URIRef  # Unit Load Device Discount
