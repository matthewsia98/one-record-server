from rdflib.namespace import DefinedNamespace, Namespace

from app.namespaces.code_lists._AIRCRAFTPOSSIBILITYCODE import AIRCRAFTPOSSIBILITYCODE
from app.namespaces.code_lists._AWBUSEINDICATOR import AWBUSEINDICATOR
from app.namespaces.code_lists._CHARGECODE import CHARGECODE
from app.namespaces.code_lists._CHARGEIDENTIFIER import CHARGEIDENTIFIER
from app.namespaces.code_lists._COMMODITYCODE import COMMODITYCODE
from app.namespaces.code_lists._DANGEROUSGOODSCODE import DANGEROUSGOODSCODE
from app.namespaces.code_lists._DEMURRAGECODE import DEMURRAGECODE
from app.namespaces.code_lists._ENTITLEMENTCODE import ENTITLEMENTCODE
from app.namespaces.code_lists._EXPLOSIVECOMPATIBILITYGROUPCODE import (
    EXPLOSIVECOMPATIBILITYGROUPCODE,
)
from app.namespaces.code_lists._GOODSTYPECODE import GOODSTYPECODE
from app.namespaces.code_lists._GOODSTYPEEXTENSIONCODE import GOODSTYPEEXTENSIONCODE
from app.namespaces.code_lists._MEASUREMENTUNITCODE import MEASUREMENTUNITCODE
from app.namespaces.code_lists._MODECODE import MODECODE
from app.namespaces.code_lists._MOVEMENTINDICATOR import MOVEMENTINDICATOR
from app.namespaces.code_lists._OTHERCHARGECODE import OTHERCHARGECODE
from app.namespaces.code_lists._PACKAGEMARKCODE import PACKAGEMARKCODE
from app.namespaces.code_lists._PACKAGINGDANGERLEVELCODE import PACKAGINGDANGERLEVELCODE
from app.namespaces.code_lists._PARTICIPANTIDENTIFIER import PARTICIPANTIDENTIFIER
from app.namespaces.code_lists._PREPAIDCOLLECTINDICATOR import PREPAIDCOLLECTINDICATOR
from app.namespaces.code_lists._RADIOACTIVEMATERIALCLASSIFICATION import (
    RADIOACTIVEMATERIALCLASSIFICATION,
)
from app.namespaces.code_lists._RATECLASSCODE import RATECLASSCODE
from app.namespaces.code_lists._RATINGSTYPE import RATINGSTYPE
from app.namespaces.code_lists._RATYPECODE import RATYPECODE
from app.namespaces.code_lists._REGULATEDENTITYCATEGORYCODE import (
    REGULATEDENTITYCATEGORYCODE,
)
from app.namespaces.code_lists._SCREENINGEXEMPTION import SCREENINGEXEMPTION
from app.namespaces.code_lists._SCREENINGMETHOD import SCREENINGMETHOD
from app.namespaces.code_lists._SECURITYSTATUS import SECURITYSTATUS
from app.namespaces.code_lists._SERVICECODE import SERVICECODE
from app.namespaces.code_lists._SHIPMENTSECURITYSTATUS import SHIPMENTSECURITYSTATUS
from app.namespaces.code_lists._SIGNATORYROLE import SIGNATORYROLE
from app.namespaces.code_lists._SIGNATURETYPECODE import SIGNATURETYPECODE
from app.namespaces.code_lists._SPACEALLOCATIONCODE import SPACEALLOCATIONCODE
from app.namespaces.code_lists._SPECIALHANDLINGCODE import SPECIALHANDLINGCODE
from app.namespaces.code_lists._STATUSCODE import STATUSCODE
from app.namespaces.code_lists._TRANSACTIONPURPOSECODE import TRANSACTIONPURPOSECODE
from app.namespaces.code_lists._TRANSPORTMEANSSERVICETYPE import (
    TRANSPORTMEANSSERVICETYPE,
)
from app.namespaces.code_lists._ULDCHARGECODE import ULDCHARGECODE
from app.namespaces.code_lists._ULDCONDITIONCODE import ULDCONDITIONCODE
from app.namespaces.code_lists._ULDLOADINGINDICATOR import ULDLOADINGINDICATOR


class CODELISTS(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:11:32.058083
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/")

    AWBUseIndicator: type[DefinedNamespace] = AWBUSEINDICATOR
    AircraftPossibilityCode: type[DefinedNamespace] = AIRCRAFTPOSSIBILITYCODE
    ChargeCode: type[DefinedNamespace] = CHARGECODE
    ChargeIdentifier: type[DefinedNamespace] = CHARGEIDENTIFIER
    CommodityCode: type[DefinedNamespace] = COMMODITYCODE
    DangerousGoodsCode: type[DefinedNamespace] = DANGEROUSGOODSCODE
    DemurrageCode: type[DefinedNamespace] = DEMURRAGECODE
    EntitlementCode: type[DefinedNamespace] = ENTITLEMENTCODE
    ExplosiveCompatibilityGroupCode: type[DefinedNamespace] = (
        EXPLOSIVECOMPATIBILITYGROUPCODE
    )
    GoodsTypeCode: type[DefinedNamespace] = GOODSTYPECODE
    GoodsTypeExtensionCode: type[DefinedNamespace] = GOODSTYPEEXTENSIONCODE
    MeasurementUnitCode: type[DefinedNamespace] = MEASUREMENTUNITCODE
    ModeCode: type[DefinedNamespace] = MODECODE
    MovementIndicator: type[DefinedNamespace] = MOVEMENTINDICATOR
    OtherChargeCode: type[DefinedNamespace] = OTHERCHARGECODE
    PackageMarkCode: type[DefinedNamespace] = PACKAGEMARKCODE
    PackagingDangerLevelCode: type[DefinedNamespace] = PACKAGINGDANGERLEVELCODE
    ParticipantIdentifier: type[DefinedNamespace] = PARTICIPANTIDENTIFIER
    PrepaidCollectIndicator: type[DefinedNamespace] = PREPAIDCOLLECTINDICATOR
    RaTypeCode: type[DefinedNamespace] = RATYPECODE
    RadioactiveMaterialClassification: type[DefinedNamespace] = (
        RADIOACTIVEMATERIALCLASSIFICATION
    )
    RateClassCode: type[DefinedNamespace] = RATECLASSCODE
    RatingsType: type[DefinedNamespace] = RATINGSTYPE
    RegulatedEntityCategoryCode: type[DefinedNamespace] = REGULATEDENTITYCATEGORYCODE
    ScreeningExemption: type[DefinedNamespace] = SCREENINGEXEMPTION
    ScreeningMethod: type[DefinedNamespace] = SCREENINGMETHOD
    SecurityStatus: type[DefinedNamespace] = SECURITYSTATUS
    ServiceCode: type[DefinedNamespace] = SERVICECODE
    ShipmentSecurityStatus: type[DefinedNamespace] = SHIPMENTSECURITYSTATUS
    SignatoryRole: type[DefinedNamespace] = SIGNATORYROLE
    SignatureTypeCode: type[DefinedNamespace] = SIGNATURETYPECODE
    SpaceAllocationCode: type[DefinedNamespace] = SPACEALLOCATIONCODE
    SpecialHandlingCode: type[DefinedNamespace] = SPECIALHANDLINGCODE
    StatusCode: type[DefinedNamespace] = STATUSCODE
    TransactionPurposeCode: type[DefinedNamespace] = TRANSACTIONPURPOSECODE
    TransportMeansServiceType: type[DefinedNamespace] = TRANSPORTMEANSSERVICETYPE
    ULDChargeCode: type[DefinedNamespace] = ULDCHARGECODE
    ULDConditionCode: type[DefinedNamespace] = ULDCONDITIONCODE
    ULDLoadingIndicator: type[DefinedNamespace] = ULDLOADINGINDICATOR
