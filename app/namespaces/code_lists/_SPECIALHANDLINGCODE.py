from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class SPECIALHANDLINGCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:48.507694
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#")

    _fail = True

    ACT: URIRef  # Active Temperature Controlled System
    AOG: URIRef  # Aircraft on Ground
    ATT: URIRef  # Goods Attached to Air Waybill
    AVI: URIRef  # Live Animal
    BIG: URIRef  # Outsized
    BUP: URIRef  # Bulk Unitization Programme, Shipper/Consignee Handled Unit
    CAO: URIRef  # Cargo Aircraft Only
    CAT: URIRef  # Cargo Attendant Accompanying Shipment
    CIC: URIRef  # Cargo may be loaded in the passenger cabin
    COL: URIRef  # Cool Goods
    COM: URIRef  # Company Mail
    CRT: URIRef  # Control Room Temperature +15°C to +25°C
    DIP: URIRef  # Diplomatic Mail
    EAP: URIRef  # e-freight Consignment with Accompanying Paper Documents
    EAT: URIRef  # Foodstuffs
    EAW: URIRef  # e-freight Consignment with No Accompanying Paper Documents
    EBI: URIRef  # Lithium ion batteries excepted as per Section II of PI 965
    EBM: URIRef  # Lithium metal batteries excepted as per Section II of PI 968
    ECC: URIRef  # Consignment established with an electronically concluded cargo contract with no accompanying paper airwaybill
    ECP: URIRef  # Consignment established with a paper air waybill contract being printed under an e-AWB agreement
    ELI: URIRef  # Lithium Ion Batteries otherwise excepted from the IATA DGR
    ELM: URIRef  # Lithium Metal Batteries otherwise excepted from the IATA DGR
    EMD: URIRef  # Electronic Monitoring Devices on/in Cargo/Container
    ERT: URIRef  # Extended Room Temperature +2°C to +25°C
    FIL: URIRef  # Undeveloped/Unexposed Film
    FRI: URIRef  # Frozen Goods Subject to Veterinary/Phytosanitary Inspections
    FRO: URIRef  # Frozen Goods
    GOH: URIRef  # Hanging Garments
    HEA: URIRef  # Heavy Cargo/150 kilograms and over per piece
    HEG: URIRef  # Hatching Eggs
    HUM: URIRef  # Human Remains in Coffin
    ICE: URIRef  # Dry Ice
    LHO: URIRef  # Living Human Organs/Blood
    LIC: URIRef  # License Required
    MAG: URIRef  # Magnetized Material
    MAL: URIRef  # Mail
    MUW: URIRef  # Munitions of War
    NSC: URIRef  # Cargo Has Not Been Secured Yet for Passenger or All-Cargo Aircraft
    NST: URIRef  # Non Stackable Cargo
    NWP: URIRef  # Newspapers, Magazines
    OBX: URIRef  # Obnoxious Cargo
    OHG: URIRef  # Overhang Item
    PAC: URIRef  # Passenger and Cargo
    PEA: URIRef  # Hunting trophies, skin, hide and all articles made from or containing parts of species listed in the CITES (Convention on International Trade in Endangered Species) appendices
    PEB: URIRef  # Animal products for non-human consumption
    PEF: URIRef  # Flowers
    PEM: URIRef  # Meat
    PEP: URIRef  # Fruits and Vegetables
    PER: URIRef  # Perishable Cargo
    PES: URIRef  # Fish/Seafood
    PHY: URIRef  # Goods subject to phytosanitary inspections
    PIL: URIRef  # Pharmaceuticals
    PIP: URIRef  # Passive Insulated Packaging
    QRT: URIRef  # Quick Ramp Transfer
    RAC: URIRef  # Reserved Air Cargo
    RBI: URIRef  # Fully regulated lithium ion batteries (Class 9, UN 3480) as per Section IA and IB of PI 965
    RBM: URIRef  # Fully regulated lithium metal batteries (Class 9, UN 3090) as per Section IA and IB of PI 968
    RCL: URIRef  # Cryogenic Liquids
    RCM: URIRef  # Corrosive
    RCX: URIRef  # Explosives 1.3C
    RDS: URIRef  # Diagnostic Specimens
    REQ: URIRef  # Excepted Quantities of Dangerous Goods
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
    RRE: URIRef  # Excepted Quantities of Radioactive Material
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
    SCO: URIRef  # Cargo Secure for All-Cargo Aircraft Only
    SHL: URIRef  # Save Human Life
    SHR: URIRef  # Secure for Passenger, All-Cargo and All-Mail Aircraft in Accordance with High Risk Requirements
    SPF: URIRef  # Laboratory Animals
    SPX: URIRef  # Cargo Secure for Passenger and All-Cargo Aircraft
    SUR: URIRef  # Surface Transportation
    SWP: URIRef  # Sporting Weapons
    VAL: URIRef  # Valuable Cargo
    VIC: URIRef  # Very Important Cargo
    VOL: URIRef  # Volume
    VUN: URIRef  # Vulnerable Cargo
    WET: URIRef  # Shipments of Wet Material not Packed in Watertight Containers
    XPS: URIRef  # Priority Small Package
