from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SIGNATORYROLE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 19:57:26.588642
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/SignatoryRole#")

    _fail = True

    APPLICANT: URIRef  # Applicant
    EXAMINING_AUTHORITY: URIRef  # Examining Authority
    ISSUING_AUTHORITY: URIRef  # Issuing Authority
    MANAGEMENT_AUTHORITY: URIRef  # Management Authority
    PERMIT_ISSUER: URIRef  # Permit Issuer
