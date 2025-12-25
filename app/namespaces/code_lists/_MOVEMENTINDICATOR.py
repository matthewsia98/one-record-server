from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class MOVEMENTINDICATOR(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 02:56:02.825770
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/MovementIndicator#")

    _fail = True

    AA: URIRef  # Actual Arrival (Touchdown)
    AB: URIRef  # Actual On-block
    AD: URIRef  # Actual Departure (Take off)
    AG: URIRef  # Actual gate in time - Relates to gate passing of trucks
    AH: URIRef  # Actual gate out time - Relates t gate passing of trucks
    AK: URIRef  # Actual end of unloading time
    AL: URIRef  # Actual end of loading time
    AO: URIRef  # Actual Off-block
    AR: URIRef  # Actual driver reporting time
    CN: URIRef  # Cancellation
    DA: URIRef  # Doc Arrival
    DL: URIRef  # Delayed
    DV: URIRef  # Diversion
    EA: URIRef  # Estimated Arrival (Touchdown)
    EB: URIRef  # Estimated On-block
    ED: URIRef  # Estimated Departure (Take off)
    EK: URIRef  # Estimated end of unloading time
    EL: URIRef  # Estimated end of loading time
    EO: URIRef  # Estimated Off-block
    ER: URIRef  # Estimated driver reporting time
    FR: URIRef  # Force Return
    NI: URIRef  # Next Information
    PA: URIRef  # Pre-announcement of the truck - to enable to pre-announce data (driver name, license plates, etc.) to GHA at departure station
    RR: URIRef  # Return to RAMP
    SA: URIRef  # Scheduled Arrival
    SD: URIRef  # Scheduled Departure
    SK: URIRef  # Scheduled end of unloading time
    SL: URIRef  # Scheduled end of loading time
    SR: URIRef  # Scheduled latest driver reporting time for collection and/or delivery
    SS: URIRef  # Scheduled earliest driver reporting time for collection and/or delivery
