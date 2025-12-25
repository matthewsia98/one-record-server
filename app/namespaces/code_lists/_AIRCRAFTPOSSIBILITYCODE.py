from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class AIRCRAFTPOSSIBILITYCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:23.273471
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#")

    _fail = True

    BBF: URIRef  # Pure freighter flight carrying Loose Load Cargo
    BBQ: URIRef  # Mixed configuration (Combi) aircraft carrying Loose Load Cargo on the passenger deck
    BBV: URIRef  # Truck carrying Loose Load Cargo
    LLF: URIRef  # Pure freighter flight carrying Containerized Cargo (ULDs)
    LLJ: URIRef  # Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)
    LLQ: URIRef  # Mixed configuration (Combi) aircraft carrying Containerized Cargo (ULDs) on the passenger deck
    LLV: URIRef  # Truck carrying Containerized Cargo (ULDs)
    LPF: URIRef  # Pure freighter flight carrying Containerized (ULDs)/Palletized Cargo
    LPJ: URIRef  # Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)/ Palletized Cargo
    LPQ: URIRef  # Mixed configuration (Combi) aircraft carrying Containerized (ULDs)/Palletized Cargo on the passenger deck
    LPV: URIRef  # Truck carrying Containerized (ULDs)/Palletized Cargo
    PPF: URIRef  # Pure freighter flight carrying Palletized Cargo
    PPJ: URIRef  # Passenger flight operated by wide-bodied aircraft carrying Palletized Cargo
    PPQ: URIRef  # Mixed configuration aircraft carrying Palletized Cargo on the passenger deck
    PPV: URIRef  # Truck carrying Palletized Cargo
