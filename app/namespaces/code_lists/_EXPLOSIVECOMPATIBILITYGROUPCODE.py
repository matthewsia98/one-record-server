from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class EXPLOSIVECOMPATIBILITYGROUPCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:08.579598
    """

    _NS = Namespace(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#"
    )

    _fail = True

    A: URIRef  # Primary explosive substance (Hazard Division 1.1)
    B: URIRef  # Article containing a primary explosive substance and not containing two or more effective protective features. Some articles, such as detonators for blasting, detonator assemblies for blasting and primers, cap type, are included, even though they do not contain primary explosives (Hazard Division 1.1; 1.2; 1.4)
    C: URIRef  # Propellant explosive substance or other deflagrating explosive substance or article containing such explosive substance (Hazard Division 1.1; 1.2; 1.3; 1.4)
    D: URIRef  # Secondary detonating explosive substance or black powder or article containing a secondary detonating explosive substance, in each case without means of initiation and without a propelling charge or article containing a primary explosive substance and containing two or more effective protective features (Hazard Division 1.1; 1.2; 1.4; 1.5)
    E: URIRef  # Article containing a secondary detonating explosive substance, without means of initiation, with a propelling charge (other than one containing a flammable liquid or gel or hypergolic liquids) or without a propelling charge (Hazard Division 1.1; 1.2; 1.4)
    F: URIRef  # Article containing a secondary detonating explosive substance, with its own means of initiation, with a propelling charge (other than one containing a flammable liquid or gel or hypergolic liquids) or without a propelling charge (Hazard Division 1.1; 1.2; 1.3; 1.4)
    G: URIRef  # Pyrotechnic substance, or article containing a pyrotechnic substance, or article containing both an explosive substance and an illuminating, incendiary, tear- or smoke-producing substance (other than a water -activated article or one containing white phosphorus, phosphide, a pyrophoric substance, a flammable liquid or get or hypergolic liquids) (Hazard Division 1.1; 1.2; 1.3; 1.4)
    H: URIRef  # Article containing both an explosive substance and white phosphorus (Hazard Division 1.2; 1.3)
    J: URIRef  # Article containing both an explosive substance and a flammable liquid or gel (Hazard Division 1.1; 1.2; 1.3)
    K: URIRef  # Article containing both an explosive substance and a toxic chemical agent (Hazard Division 1.1; 1.3)
    L: URIRef  # Explosive article or substance containing an explosive substance and presenting a special risk (e.g. due to water activation, or the presence of hypergolic liquids, phosphides or a pyrophoric substance) and needing isolation of each type (Hazard Division 1.2; 1.2; 1.3)
    N: URIRef  # Article containing only extremely insensitive detonating substances (Hazard Division 1.6)
    S: URIRef  # Article or substance so packed or designed that any hazardous effects arising from accidental functioning are confined within the package unless the package has been degraded by fire, in which case all blast or projection effects are limited to the extent that they do not significantly hinder or prohibit fire fighting or other emergency response efforts in the immediate vicinity of the package (Hazard Division 1.4)
