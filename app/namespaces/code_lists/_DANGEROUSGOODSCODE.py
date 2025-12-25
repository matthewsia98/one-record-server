from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class DANGEROUSGOODSCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:26.733041
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#")

    _fail = True

    CAO: URIRef  # Cargo Aircraft Only
    EBI: URIRef  # Lithium ion batteries excepted as per Section II of PI 965
    EBM: URIRef  # Lithium metal batteries excepted as per Section II of PI 968
    ELI: URIRef  # Lithium Ion Batteries otherwise excepted from the IATA DGR
    ELM: URIRef  # Lithium Metal Batteries otherwise excepted from the IATA DGR
    ICE: URIRef  # Dry Ice
    MAG: URIRef  # Magnetized Material
    RBI: URIRef  # Fully regulated lithium ion batteries (Class 9, UN 3480) as per Section IA and IB of PI 965
    RBM: URIRef  # Fully regulated lithium metal batteries (Class 9, UN 3090) as per Section IA and IB of PI 968
    RCL: URIRef  # Cryogenic Liquids
    RCM: URIRef  # Corrosive
    RCX: URIRef  # Explosives 1.3C
    REX: URIRef  # To be reserved for normally forbidden Explosives, Divisions 1.1, 1.2, 1.3, 1.4F, 1.5 and 1.6
    RFG: URIRef  # Flammable Gas
    RFL: URIRef  # Flammable Liquid
    RFS: URIRef  # Flammable Solid
    RFW: URIRef  # Dangerous When Wet
    RGX: URIRef  # Explosives 1.3G
    RIS: URIRef  # Infectious Substance
    RLI: URIRef  # Fully Regulated Lithium Ion Batteries (Class 9)
    RLM: URIRef  # Fully Regulated Lithium Metal Batteries (Class 9)
    RMD: URIRef  # Miscellaneous Dangerous Goods
    RNG: URIRef  # Non-Flammable Non-Toxic Gas
    ROP: URIRef  # Organic Peroxide
    ROX: URIRef  # Oxidizer
    RPB: URIRef  # Toxic Substance
    RPG: URIRef  # Toxic Gas
    RRW: URIRef  # Radioactive Material Category I-White
    RRY: URIRef  # Radioactive Material Categories II-Yellow and III-Yellow
    RSB: URIRef  # Polymeric Beads
    RSC: URIRef  # Spontaneously Combustible
    RXB: URIRef  # Explosives 1.4B
    RXC: URIRef  # Explosives 1.4C
    RXD: URIRef  # Explosives 1.4D
    RXE: URIRef  # Explosives 1.4E
    RXG: URIRef  # Explosives 1.4G
    RXS: URIRef  # Explosives 1.4S
