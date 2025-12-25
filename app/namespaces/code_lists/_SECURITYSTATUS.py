from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SECURITYSTATUS(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 02:56:08.619790
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/SecurityStatus#")

    _fail = True

    NSC: URIRef  # Cargo Has Not Been Secured Yet for Passenger or All-Cargo Aircraft
    SCO: URIRef  # Cargo Secure for All-Cargo Aircraft Only
    SHR: URIRef  # Secure for Passenger, All-Cargo and All-Mail Aircraft in Accordance with High Risk Requirements
    SPX: URIRef  # Cargo Secure for Passenger and All-Cargo Aircraft
