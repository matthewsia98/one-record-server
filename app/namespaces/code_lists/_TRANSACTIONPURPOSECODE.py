from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class TRANSACTIONPURPOSECODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:28.877320
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#")

    _fail = True

    B: URIRef  # Breeding in captivity or artificial propagation
    E: URIRef  # Educational
    G: URIRef  # Botanical garden
    H: URIRef  # Hunting trophy
    L: URIRef  # Law enforcement / judicial / forensic
    M: URIRef  # Medical (including biomedical research)
    N: URIRef  # Reintroduction or introduction into the wild
    P: URIRef  # Personal
    Q: URIRef  # Circus or travelling exhibition
    S: URIRef  # Scientific
    T: URIRef  # Commercial
    Z: URIRef  # Zoo
