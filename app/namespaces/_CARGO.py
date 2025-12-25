from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class CARGO(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:03:17.193640
    """

    _NS = Namespace("https://onerecord.iata.org/ns/cargo#")

    _fail = True

    ACCELEROMETER: URIRef  # Indicates the sensor type as accelerometer
    ACTIVE: URIRef  # Used when a LogisticsActivity is active
    ACTUAL: URIRef  # Used when a time is actual
    ALTERNATE_EMAIL_ADDRESS: (
        URIRef  # Indicates a contact detail as alternate email address
    )
    ALTERNATE_PHONE_NUMBER: (
        URIRef  # Indicates a contact detail as alternate phone number
    )
    AccountNumber: URIRef  #
    AccountType: URIRef  # Open code list for Account types
    AccountingNote: URIRef  # Embedded object used for AWB mapping (box 10)
    ActionTimeType: URIRef  # Restricted code list for acceptable action times
    ActivitySequence: URIRef  # Embedded object to create a sequence of Activities in the context of a Service
    Actor: (
        URIRef  # Superclass: Actors are Persons or entities acting like a single person
    )
    Address: URIRef  # Address details
    Adjustments: URIRef  # Adjustments in the context of CASS records
    Answer: URIRef  # Answer holds the answer to one Question
    BOOKABLE: URIRef  # Used when a booking option (or proposal) is bookable
    BOOKED: URIRef  # Used when a booking option proposal is booked
    BULK: URIRef  # Indicates the load type as bulk
    BillingDetails: URIRef  # In the context of CASS2. process, BillingDetails object is used to integrate specific Billing and Settlement data requirements
    Booking: URIRef  # Booking object refers to a confirmed booking
    BookingOption: URIRef  # Booking details
    BookingOptionRequest: (
        URIRef  # Request object, refers to the Quote request or Booking request
    )
    BookingOptionStatus: (
        URIRef  # Restricted code list containing the statuses of a booking option
    )
    BookingPreferences: URIRef  # BookingPreferences details
    BookingRequest: URIRef  # A party, usually the freight forwarder, creates the BookingRequest in order to confirm the booking to the Carrier
    BookingSegment: URIRef  # Information about the booking status on segment level, assigning pieces and ULDs to a TransportLeg with a Space Allocation Code
    BookingShipment: URIRef  # Simplified shipment object that is to be used only for the distribution scope where only a subset of data is known priori to operational phase.
    BookingStatus: (
        URIRef  # Restricted code list containing the possible statuses of a booking
    )
    BookingTimes: URIRef  # Previously called Schedule. This object refers to times used for the Booking Option Request (preferences part of the request) or the Booking Option (times sur as LAT where there is a commitment from the carrier)
    CANCELLED: URIRef  # Used when a LogisticsActivity is cancelled
    CO2Emissions: URIRef  # CO2 Calculation
    COMPLETE: URIRef  # Used when a LogisticsActivity is complete
    COMPOSITION: URIRef  # Describes a composition, for example the loading of a container or the build-up of an ULD
    CONFIRMED: URIRef  # Used when a booking is confirmed
    CONSIGNEE: URIRef  # Consignee's Account
    CONSIGNOR: URIRef  # Consignor
    CUSTOMER_CONTACT: URIRef  # Indicates a contact person as customer contact
    CUSTOMS_CONTACT: URIRef  # Indicates a contact person as customs contact
    Carrier: URIRef  # Company details of carriers
    CarrierProduct: URIRef  # Carrier product details
    Characteristic: URIRef  # Product additional details
    Check: URIRef  # Action to describe a check
    CheckTemplate: URIRef  # Body of a Check referencing various Questions
    CheckTotalResult: URIRef  # Result of a Check
    CodeListElement: URIRef  # Embedded object to transmit codes from non-RDF code lists in 1R in a semi-structured way. Code lists may be externally maintained codes (such as HS codes) or carrier-specific codes. If a code is present in RDF-form as Named Individual (like in the 1R core code lists ontology), it suffices to put in its IRI
    Company: URIRef  # Company details
    Composing: URIRef  # Action to describe build-up or break-down of LoadingUnits
    CompositionType: URIRef  # Restricted code list for Composing subtypes
    ContactDetail: URIRef  # Contact details
    ContactDetailType: URIRef  # Open code list for types of contact details
    ContactRole: URIRef  # Open code list for roles of a contact
    CurrencyValue: URIRef  # Embedded object to transmit currencies
    CustomsInformation: URIRef  # Customs information details
    DECOMPOSITION: URIRef  # Describes a decomposition, for example the unloading of a container or the break-down of an ULD
    DELETED: URIRef  # Used when a booking is deleted
    DIRECT: URIRef  # Indicates a Direct waybill
    DgDeclaration: URIRef  # Dangerous goods declaration
    DgProductRadioactive: URIRef  # Details of the radioactive products
    DgRadioactiveIsotope: (
        URIRef  # Details of the radioactive isotope contained in the product
    )
    Dimensions: URIRef  # Dimension details
    DirectionType: URIRef  # Restricted code list for the direction of a MovementTime
    EMAIL_ADDRESS: URIRef  # Indicates a contact detail as email address
    EMERGENCY_CONTACT: URIRef  # Indicates a contact person as emergency contact
    ESTIMATED: URIRef  # Used when a time is estimated
    EXPECTED: URIRef  # Used when a time is expected
    EXPIRED: URIRef  # Used when a booking option proposal is expired
    EpermitConsignment: URIRef  # Details of the pieces (Live animals) of the permit and specific information such as quantity measured and used to date quota
    EpermitSignature: URIRef  # Signature details of the Epermit for Live Animals
    EventTimeType: URIRef  # Restricted code list for acceptable event times
    ExecutionStatus: (
        URIRef  # Restricted code list for the execution status of activities
    )
    ExternalReference: URIRef  # Reference documents details
    FAX_NUMBER: URIRef  # Indicates a contact detail as fax number
    FF: URIRef  # Freight Forwarder Account
    GEOLOCATION: URIRef  # Indicates the sensor type as geolocation
    Geolocation: URIRef  # Geolocation details - e.g. for drones, automated vehicles
    HOUSE: URIRef  # Indicates a House Waybill
    HUMIDITY: URIRef  # Indicates the sensor type as humidity
    HandlingService: URIRef  # Generic handling service for non main carriage activities
    INBOUND: URIRef  # Indicates the described direction in a movement time as inbound
    Insurance: URIRef  # Insurance details
    IotDevice: URIRef  # IoT Device details
    Item: URIRef  # Item details
    ItemDg: URIRef  # Dangerous Goods subtype of Item
    LIGHT: URIRef  # Indicates the sensor type as light
    LOADING: URIRef  # Describes a loading process, for example putting an ULD on an aircraft or a piece in a truck
    LOOSE: URIRef  # Indicates the load type as loose
    LineItemPackage: (
        URIRef  # Grouping of pieces for rating information as per Waybill box 22I
    )
    LiveAnimalsEpermit: URIRef  # Epermit for Live Animals details
    LoadType: URIRef  # Restricted code list for the Load Type of a piece or shipment
    Loading: URIRef  # Action to describe onloading or offloading TransportMeans
    LoadingMaterial: URIRef  # LoadingMaterial describes transportable, complementary non-Piece objects such as dry ice or nets
    LoadingType: URIRef  # Restricted code list for Loading subtypes
    LoadingUnit: URIRef  # Common loading unit/container details
    Location: URIRef  # Location describes a physical location, e.g. an airport, a warehouse or a truck deck
    LogisticsAction: URIRef  # Superclass: LogisticsAction is a specific task with a specific result performed on one or more physical LOs by one party in the context of an Activity
    LogisticsActivity: URIRef  # Superclass: LogisticsActivity is a scheduled set of tasks that is executed as part of one or more Services
    LogisticsAgent: URIRef  # Superclass: LogisticsAgents describe acting entities in the logistics supply chain such as persons and organizations
    LogisticsEvent: URIRef  # Event details
    LogisticsObject: URIRef  # Logistics Object parent class, containing all common properties for logistics objects.
    LogisticsService: URIRef  # Superclass: LogisticsService is a sequence of Activities provided by one Party to another
    LoosePiece: URIRef  # LoosePiece details
    MAIN_CARRIAGE: URIRef  # Indicates the mode qualifier as main carriage
    MASTER: URIRef  # Indicates a Master Waybill
    Measurement: URIRef  # Measurements details for Sensors, either generic or geolocation measurements are recorded
    ModeQualifier: URIRef  # Open code list for transport modes
    MovementTime: URIRef  # Times referring to Transport Movements, used to describe specfic times such as Actual Departure time, etc.
    MovementTimeType: URIRef  # Restricted code list for MovementTime subtypes
    NONBOOKABLE: URIRef  # Used when a booking option is nonbookable
    NOT_BOOKABLE: URIRef  # Used when a booking option proposal is not bookable
    NonHumanActor: (
        URIRef  # Non-human actors are actors which are not a person, such as robots
    )
    ON_CARRIAGE: URIRef  # Indicates the mode qualifier as on carriage
    ON_REQUEST: URIRef  # Used when a booking option proposal is on request
    OUTBOUND: URIRef  # Indicates the described direction in a movement time as outbound
    Organization: URIRef  # Superclass: Organizations represent a kind of Agent corresponding to social institutions such as companies, societies, etc
    OtherCharge: URIRef  # Other Charge details from AWB as per bullet point 19 - data element 23 from AWB
    OtherIdentifier: URIRef  # Other identifiers
    PALLET: URIRef  # Indicates the load type as pallet
    PENDING: URIRef  # Used when a LogisticsActivity is pending
    PHONE_NUMBER: URIRef  # Indicates a contact detail as phone number
    PLANNED: URIRef  # Used when a time is planned
    PRESSURE: URIRef  # Indicates the sensor type as pressure
    PRE_CARRIAGE: URIRef  # Indicates the mode qualifier as pre carriage
    PackagingType: URIRef  # Packaging details
    Party: URIRef  # Refers to a Company and its role in a specific context, e.g Company A as shipper. Cargo-XML Code List 1.15 can be used as a reference with the addition of "Notify Party"
    Person: URIRef  # Person details
    PhysicalLogisticsObject: URIRef  # Superclass: PhysicalLogisticObjects represent the digital twin of an object in the logistics supply chain that physically exist
    Piece: URIRef  # Individual piece or virtual grouping of pieces
    PieceDg: URIRef  # Dangerous Goods subtype of Piece
    PieceGroup: URIRef  # PieceGroup details
    PieceLiveAnimals: URIRef  # LiveAnimals subclass of Piece
    Price: URIRef  # Price associated to the offer/booking
    Product: URIRef  # Product details
    ProductDg: URIRef  # Dangerous Goods subtype of Product
    PublicAuthority: URIRef  # PublicAuthorities are Organizations of the state on public interests, such as customs
    QUEUED: URIRef  # Used when a booking or booking option is queued or pending
    Question: URIRef  # Question as part of a CheckTemplate
    REJECTED: URIRef  # Used when a booking is rejected
    REQUESTED: URIRef  # Used when a time is requested
    Ranges: URIRef  # Ranges details
    Ratings: URIRef  # Ratings details
    RegulatedEntity: URIRef  # Regulated Entity
    SCHEDULED: URIRef  # Used when a time is scheduled
    STORE_IN: URIRef  # Describes a store-in process, where a physical object is assigned to a specific location
    STORE_OUT: URIRef  # Describes a store-out process, where a physical object leaves a specific location
    SecurityDeclaration: URIRef  # Security declaration details
    Sensor: URIRef  # Sensor details and measurements, linked to Connected Devices
    SensorType: URIRef  # Open code list for sensor types
    Shipment: URIRef  # Shipment details
    StationRemarks: URIRef  # StationRemarks details
    Storage: URIRef  # Activity to describe storing processes
    Storing: URIRef  # Action to describe store-in or store-out
    StoringType: URIRef  # Restricted code list for Storing subtypes
    TELEX: URIRef  # Indicates a contact detail as telex
    THERMOMETER: URIRef  # Indicates the sensor type as thermometer
    TILT: URIRef  # Indicates the sensor type as tilt
    TemperatureInstructions: URIRef  # TemperatureInstructions details
    TransportLegs: URIRef  # TransportLegs details
    TransportMeans: URIRef  # Transport means details
    TransportMovement: URIRef  # Activity to describe transports, replaces the TransportSegment in v1.1 and above
    ULD: URIRef  # Unit Load Device details
    ULDBasicPiece: URIRef  # ULDBasicPiece details
    ULDSpecificPiece: URIRef  # ULDSpecificPiece details
    UNIT_LOAD_DEVICE: URIRef  # Indicates the load type as uld
    UNLOADING: URIRef  # Describes an unloading process, for example removing an ULD from an aircraft or a piece from a truck
    UNPLANNED_STOP: (
        URIRef  # Indicates the that the movement time describes an unplanned stop
    )
    UnitComposition: (
        URIRef  # Activity to describe composition and decomposition of LoadingUnits
    )
    UnitsPreference: URIRef  # UnitsPreference details
    VIBRATION: URIRef  # Indicates the sensor type as vibration
    Value: URIRef  # Unit of measurement details
    VolumePieceGroup: URIRef  # VolumePieceGroup details
    VolumetricWeight: URIRef  # Volumetric weight details
    WEBSITE: URIRef  # Indicates a contact detail as website
    Waybill: URIRef  # Waybill details
    WaybillLineItem: URIRef  # Information from AWB Rate Description section as per bullet point 18 - data elements 22A - 22Z from AWB. Data describing Piece and Package parameters to be transmitted per Piece object using pieceReferences; Data describing ULD parameters to be transmitted per ULD object using uldReference.
    WaybillType: URIRef  # Restricted code list for Waybill types
    accountNumberType: URIRef  # Type of the account of the account number
    accountNumbers: URIRef  # Information about account numbers
    accountingInformation: URIRef  # Indicates the details of accounting information. Free text e.g. PAYMENT BY CERTIFIED CHEQUE etc.
    accountingNoteIdentifier: (
        URIRef  # String holding accounting information (AWB box 10)
    )
    accountingNoteText: (
        URIRef  # String holding the identifier in an accounting note (AWB box 10)
    )
    accountingNotes: URIRef  # Information about accounting notes (AWB box 10)
    acquisitionDateTime: URIRef  # Defined in Resolution Conf. 13.6 and is required for pre-Convention specimens (box 12b)
    actionEndTime: URIRef  # DateTime holding the end time of the Action; Type is indicated through ActionType property
    actionStartTime: URIRef  # DateTime holding the start time of the Action; Type is indicated through ActionType property
    actionTimeType: URIRef  # Enum stating the type of the Action
    activity: URIRef  # Reference to the Activity that is performed as part of a Service
    activityLevelMeasure: (
        URIRef  # Numeric expression of the activity of a radioactive Item
    )
    activitySequences: URIRef  # Information about the Activities that are part of the Service and their sequence
    additionalHazardClassificationId: URIRef  # Identifies the subsidiary hazard class / division identification containing a numeric field separated by a decimal. There may be , 1 or 2 subsidiary risk classes or divisions. If there is more than one, each should be separated by a comma. The subsidiary risk must be shown in parentheses.
    additionalInformation: URIRef  # Additional information related to the Booking Option, e.g. sales details
    additionalSecurityInformation: URIRef  # Any additional information that may be required by an ICAO Member State
    address: URIRef  # Address details
    addressCode: (
        URIRef  # Address identifier using special coding systems e.g. US CBP FIRMS code
    )
    adjustments: URIRef  # Information about Adjustments performed on the BillingDetails
    aircraftLimitationInformation: URIRef  # Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air)
    aircraftPossibilityCode: URIRef  # Type of aircraft to be used if any specific requirements (e.g. Pure freighter, etc.)
    airlineCode: URIRef  # IATA two-character airline code
    allPackedInOneIndicator: URIRef  # A statement identifying that the dangerous goods listed above are all contained in the same outer packaging. Takes the form All packed in one aaaa (description of packaging type) x nn (number of packages). Applies to air transport only. (Air)
    allotmentCode: URIRef  # String holding an allotment code of a booking segment
    alternatives: URIRef  # Description of the alternatives proposed that do not match the Booking Option Request
    annualQuotaQuantity: URIRef  # total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    answer: URIRef  # Reference to the Answer to the Question
    answerActor: URIRef  # Reference to the Actor giving the Answer
    answerOptionsText: URIRef  # Text restrictions to the Answer
    answerOptionsValue: URIRef  # Value restrictions to the answer
    answerValue: URIRef  # Information about an answer Value of any kind of the Answer
    appliedOnPieces: URIRef  # Piece on which the Packaging type is applicable
    arrivalDate: URIRef  # Arrival date and time of the leg
    arrivalLocation: URIRef  # Reference to the arrival Location
    associatedEpermit: (
        URIRef  # Reference to the permits associated with the Live Animals
    )
    associatedOrganization: (
        URIRef  # Reference to the Organization the Actor is associated with
    )
    ataDesignator: URIRef  # US / ATA Unit Load Device type code e.g. M2
    attachedIotDevices: URIRef  # References to all connected IotDevices
    attachedToObject: (
        URIRef  # Reference to the PhysicalLogisticsObject the IotDevice is attached to
    )
    authorizationInformation: URIRef  # Contains additional information relating to an approval, permission or other specific detail applicable to the commodity (e.g. Dangerous Goods in excepted quantities)
    awbAcceptanceDate: URIRef  # The Date AWB Acceptance should be the same as the Date AWB Delivery. (beginning of the process)
    awbDeliveryDate: URIRef  # The Date AWB Delivery is also used as the AWB Execution date which will determine which billing period it will be processed and billed in.
    awbExecutionDate: URIRef  # The AWB execution date determines which billing period the document will be processed and billed in.
    awbUseIndicator: URIRef  # It must either contain the values of R for Revenue AWB, V for Void AWB or S for Service AWB.
    basedAtLocation: URIRef  # Reference to the Location where the Organization is based at or headquartered
    batchNumber: URIRef  # Production batch number / reference
    billingChargeIdentifier: URIRef  # Billing charge identifiers to be used for CASS. Refer to CargoXML Code List 1.33
    billingDetails: URIRef  # Reference to the BillingDetails of the Waybill
    booking: URIRef  # Reference to the Booking
    bookingOptions: URIRef  # Reference to all Booking Options
    bookingPreference: URIRef  # Reference to the Booking preferences
    bookingRequest: URIRef  # Reference to the Booking Request
    bookingSegments: URIRef  # Information about booking segments - physics allocated to a specific transport leg
    bookingShipmentDetails: URIRef  # Reference to the BookingShipment if required
    bookingStatus: URIRef  # Status of the Booking
    bookingTimes: (
        URIRef  # Information about the Booking Times of a provided Booking Option
    )
    bookingToUpdate: URIRef  # Reference to the Booking to update
    calculatedEmissions: URIRef  # CO2 emissions calculated
    calculationFor: URIRef  # Reference to the TransportMovement or TransportLegs the CO2Emissions have been calculated for
    carrier: URIRef  # Reference to the operating carrier
    carrierChargeCode: URIRef  # One letter charge code as per bullet point 12 - data element 13 from AWB
    carrierDeclarationDate: (
        URIRef  # Date upon which the certification is made by the carrier
    )
    carrierDeclarationPlace: URIRef  # Location of individual or company involved in the movement of a consignment or Coded representation of a specific airport/city code
    carrierDeclarationSignature: URIRef  # Contains the authentication of the Carrier
    carrierProduct: URIRef  # Reference to the Carrier product if known
    categoryCode: URIRef  # Operations code ID. Refers to the number of the registered captive-breeding or artificial propagation operation (box 12b)
    certifiedByActor: (
        URIRef  # Reference to the Actor certifying the result of the Check if required
    )
    characteristicType: URIRef  # Product characteristics code - e.g. CLR - Color. Not restricted to a list.
    chargeCode: URIRef  # Charge code, refer to CargoXML Code List 1.1
    chargeDescription: URIRef  # Description of the charge e.g. Airfreight, fuel, etc.
    chargePaymentType: URIRef  # Indicates if charge is prepaid or collect (P, C)
    chargeQuantity: (
        URIRef  # Double describing the time or item basis quantity of a charge
    )
    chargeType: URIRef  # Charge type related to amount total as per bullet points 2/21 - data elements 24A - 3B  from AWB
    chargeableWeight: URIRef  # Chargeable weight
    chargeableWeightForRate: (
        URIRef  # Chargeable weight for which the rate description details apply
    )
    checkActions: URIRef  # References to CheckActions performed for the Activity
    checkRemark: URIRef  # Free text remarks to the check result
    checkTemplate: URIRef  # Reference to the CheckTemplate the Question is from
    checkTotalResult: URIRef  # Reference to the result of the Check
    checkedObject: URIRef  # Reference to the checked Object
    checker: URIRef  # Reference to the Actor performing the Check
    checks: URIRef  # References to the CheckActions performed on the object
    checksum: URIRef  # Checksum of the document to validate its integrity
    cityCode: URIRef  # UN/LOCODE city code (5 letter) or IATA city code (3 letter)
    cityName: URIRef  # String holding a city name
    co2Emissions: URIRef  # References to CO2Emissions
    code: URIRef  # Code or short version of a code, for example "CH" for Switzerland when referring to the UN/LOCODE code list
    codeDescription: URIRef  # Description or long version of the code, for example "Switzerland" for Switzerland when referring to the UN/LOCODE code list
    codeLevel: URIRef  # Integer indicating the level of a code if a codelists is hierarchical, for example HS-Codes
    codeListName: URIRef  # Official name of the code list without version number when direct reference is not possible, for example "UN/LOCODE" when referring to the UN/LOCODE code list
    codeListReference: URIRef  # URL to access the code list the code is taken from, for example "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory" for UN/LOCODE.
    codeListVersion: URIRef  # Version of the code list, for example "223-1" for UN/LOCODE. Used if the property codeListName is used or the version is not apparent from the resource referred to in property codeListReference.
    coload: URIRef  # Coload indicator for the pieces (boolean)
    commission: URIRef  # The commission amount in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    commissionIndicator: URIRef  # Indicates if commission is applied. Boolean
    commissionPercentage: URIRef  # The commission percentage in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    commodityItemNumber: URIRef  # Indicates the specific commodity on which the rate class code is applied
    commodityItemNumberForRate: URIRef  # Indicates the specific commodity on which the rate class code is applied
    complianceDeclarationText: URIRef  # Contains the warning message complying with the regulations text note. This field is mandatory for air (Air)
    composedMaterials: (
        URIRef  # References to the Materials being built-up or broken-down
    )
    composedPieces: URIRef  # References to the Pieces being built-up or broken-down
    compositionActions: (
        URIRef  # References to all CompositionActions performed for the UnitComposition
    )
    compositionIdentifier: URIRef  # Short text holding the process number if necessary
    compositionType: URIRef  # Enum stating whether the CompositionAction describes build-up or break-down
    connectedSensors: URIRef  # Reference to the sensors linked to the device
    consignee: URIRef  # Reference to the Organization that fulfills the role of the consignee, for a LiveAnimalsEpermit it has to include complete name and address (box 3)
    consignmentItems: URIRef  # Reference to te pieces (Live Animals) of the permit
    consignments: URIRef  # Reference to the pieces and properties linked to the Permit (box 7 to 12)
    consignorDeclarationSignature: URIRef  # Name of consignor signatory
    consolidationIndicator: URIRef  # Indication if the shipment is a consolidation
    contactDetailType: (
        URIRef  # Type of the contact details, e.g. Phone number, Mail address
    )
    contactDetails: URIRef  # Information about contactDetails
    contactPersons: (
        URIRef  # References to Actors (Person, NonHumanActor) acting as contacts
    )
    contactRole: URIRef  # Contact type - e.g. Emergency contact, Customs contact, Customer contact
    containedItems: URIRef  # Reference to the item(s) contained in the piece
    containedPieces: URIRef  # Details of contained piece(s)
    contentCode: URIRef  # Customs, Security and Regulatory Control Information Identifier. Coded indicator qualifying Customs related information: Item Number "I", Exemption Legend "L", System Downtime Reference "S", Unique Consignment Reference Number "U", Movement Reference Number "M" . Refers to Code List 1.1. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    contentOfDgProductRadioactive: (
        URIRef  # Reference to the DgProductRadioactive this Isotope is contained in
    )
    contentProductionCountry: URIRef  # Goods production country, mandatory when there are no Items. Refer ISO 3166-2
    contentProducts: URIRef  # Reference to the Products describing the content of the Piece, mandatory if no data on Item level is used
    conversionFactor: URIRef  # Volume to weight conversion factor
    copyIndicator: URIRef  # Indicates if the permit is a copy (true) or an original (false) (box 1)
    correctionNumber: URIRef  # Number of the adjustment
    correctionSerialNumber: URIRef  # Serial Number of the correction
    country: URIRef  # Country details. Refer ISO 3166-2
    coveringOrganization: URIRef  # Party covering the insurance
    createdAtLocation: (
        URIRef  # Location of the document, e.g. location where the document was emitted
    )
    creationDate: URIRef  # DateTime at which the LogisticsEvent was posted
    criticalitySafetyIndexNumeric: URIRef  # Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    currency: URIRef  # Preferred unit for currency
    currencyUnit: URIRef  # Information about the currency used in a CurrencyValue. Create an instance of CurrencyCode based on ISO 4217
    customsInformation: URIRef  # Customs details
    customsOriginCode: URIRef  # Code indicating the origin of goods for Customs purposes (e.g. For goods in free circulation in the EU) List to be provided by local authorities
    damageFlag: URIRef  # Indicates if the ULD is Damaged
    date: URIRef  # DateTime on which the CheckTemplate was released
    declarationDate: URIRef  # Date and time at which the DgDeclaration was declared
    declarationPlace: (
        URIRef  # Reference to the Location the DgDeclaration was declared at
    )
    declaredValueForCarriage: (
        URIRef  # The value of a shipment declared for carriage purposes
    )
    declaredValueForCustoms: (
        URIRef  # The value of a shipment declared for customs purposes
    )
    demurrageCode: URIRef  # Contains three designator of demurrage code, refer to RP 1654 (BCC, HHH, XXX, ZZZ)
    densityGroupCode: URIRef  # Density Group Code as defined in cXML code list 2
    department: URIRef  # Department / Division / Unit
    departureDate: URIRef  # Departure date and time of the leg
    departureLocation: URIRef  # Reference to the departure Location
    describedObjects: (
        URIRef  # Reference to the Items or Pieces in which the product can be found.
    )
    description: URIRef  # Natural language description if required
    destinationCharges: URIRef  # Charges levied at destination accruing to the last carrier, in destination currency
    destinationCurrencyRate: URIRef  # Conversion rate applied
    detailedWaybill: URIRef  # Reference to the Waybill
    deviceModel: URIRef  # Commercial denomination of the device
    dgDeclaration: URIRef  # Reference to the Dangerous Goods declaration
    dgRaTypeCode: URIRef  # The category of the package or all packed in one. Complete text to be transmitted: I-White, II-Yellow, III-Yellow instead of I, II, III
    dgRadioactiveMaterial: URIRef  # Dg Radioactive Material
    dimensions: URIRef  # Dimensions details
    dimensionsForRate: URIRef  # Information about the Dimensions used for the rate described by the Line Item
    dimensionsUnit: URIRef  # Preferred unit for measurement and dimensions
    direction: URIRef  # Direction to indicate if it's Inbound or Outbound
    discount: URIRef  # This is used as a discount to the “official” transportation charge on AWB to arrive at actual selling price
    distanceCalculated: URIRef  # Information about the calculated distance
    distanceMeasured: URIRef  # Information about the measured distance
    documentIdentifier: URIRef  # Unique document identifier
    documentLink: (
        URIRef  # Link to the document, e.g. URL of the file where it is hosted
    )
    documentName: URIRef  # If no DocumentType provided, name of the referenced document
    documentType: URIRef  # Type of the referenced document . Can refer UNEDIFACT 11  e.g. 740 - Air Waybill, but not limited to
    documentVersion: URIRef  # Document version number
    documents: URIRef  # Linked documents to the person, e.g. driver's license, ID, etc.
    dryIceWeight: URIRef  # Weight of dry ice
    earliestAcceptanceTime: (
        URIRef  # Earliest acceptance date time (requested or proposed)
    )
    elevation: URIRef  # Elevation from sea level - Change of data type to Value as of ontology v1.1
    emergencyContact: URIRef  # Contains the Emergency contact name (e.g. the name of the agency) and phone number (min required)
    employeeId: URIRef  # Employee ID
    entitlement: URIRef  # Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    epermit: URIRef  # Reference to the Epermit of the consignment
    epermitNumber: URIRef  # The original number is a unique number allocated to each document by the relevant Management Authority. (box 1)
    eventCode: URIRef  # Movement or milestone code. Can hold a named individual of the StatusCode core code list (corresponding to cXML code list 1.18), but can also be referring to different code lists.
    eventDate: URIRef  # Date and time of the event
    eventFor: URIRef  # Refers to the URI of the linked object(s)
    eventLocation: URIRef  # Location of event
    eventName: URIRef  # If no EventCode provided, event name - e.g. Security clearance
    eventTimeType: URIRef  # Indicates type of event e.g.  Scheduled, Estimated, Actual
    events: URIRef  # Events object
    examiningQuantity: URIRef  # Quantity measured by the examining authority (box 14)
    exchangeRate: URIRef  # The Rate at which the Air Waybill Amount has been multiplied to arrive at the amount of settlement.
    excludedViaPoints: URIRef  # Locations of excluded Via Points
    exclusiveUseIndicator: URIRef  # Indicates an exclusive use shipment
    executionStatus: URIRef  # Enum stating the status of the Activity
    expectedCommodity: URIRef  # Expected commodity of the shipment as per Commodity Code list. Either this or expected HS code required
    expectedHScode: URIRef  # Expected commodity of the shipment as per HS code (at least 6 digits). Either this or expectedCommodityCode required
    expiryDate: URIRef  # Product expiry date - e.g. for perishables goods or goods with programmed obsolescence
    explosiveCompatibilityGroupCode: URIRef  # Specifies the reference to the group which identifies the kind of substances and articles that are deemed to be compatible. Mandatory field in case of transport of explosive articles or substances
    exportTradeCountry: URIRef  # Country of last re-export (box 12a). Refer ISO 3166-2
    externalReferences: URIRef  # References to all associated ExternalReferences
    firstName: URIRef  # First name / given name
    fissileExceptionIndicator: URIRef  # Indicates if Fissile is excepted
    fissileExceptionReference: URIRef  # Fissile exception reference, mandatory if Fissile Exception Indicator is true.
    forBookingOption: (
        URIRef  # Reference to the BookingOption the LogisticsObject is detailing
    )
    forBookingOptionRequest: URIRef  # Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    forBookingRequest: (
        URIRef  # Reference to the Booking Request the of the Booking Option
    )
    forEpermit: URIRef  # Reference to the LiveAnimalsEpermit this Signature applies to
    forPrices: URIRef  # Reference to the Prices based on this Ratings
    forProductDg: URIRef  # Reference to the ProductDg this DgProductRadioactive details
    fuelAmountCalculated: URIRef  # Information about the calculated fuel amount
    fuelAmountMeasured: URIRef  # Information about the measured fuel amount
    fuelType: URIRef  # e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]
    fulfillsUldTypeCode: URIRef  # Text holding an ULD Type Code if the Piece fulfills it before UnitComposition
    geolocation: URIRef  # Geolocation details
    givenAtLocation: URIRef  # Reference to the Location from which the Question was answered, relevant for split checks with documentary and physical elements
    goodsDescription: URIRef  # Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    goodsDescriptionForRate: (
        URIRef  # Goods description used in the rate described by the Line Item
    )
    goodsTypeCode: URIRef  # Appendix number of the convention (I, II or III) (box 1)
    goodsTypeExtensionCode: (
        URIRef  # Appendix number of the convention (I, II or III) (box 1)
    )
    grandTotal: URIRef  # Total price
    grossWeight: URIRef  # Weight details
    grossWeightForRate: (
        URIRef  # Gross weight for which the rate description details apply
    )
    groundsForExemption: URIRef  # Exemption code - e.g. BIOM- Bio-Medical Samples SMUS - small undersized shipments MAIL - mail BIOM - bio-medical samples DIPL - diplomatic bags or diplomatic mail LFSM - life-saving materials NUCL - nuclear materials TRNS - transfer or transshipment
    handlingInformation: URIRef  # Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances.
    handlingServiceFor: URIRef  #
    hazardClassificationId: URIRef  # Identifies the hazard class / division identification containing a numeric field separated by a decimal
    height: URIRef  # Height
    houseWaybills: URIRef  # Refers to the Waybill(s) contained
    hsCode: URIRef  # Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    hsCodeForRate: URIRef  # Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    hsCommodityDescription: URIRef  # Commodity description
    hsCommodityName: URIRef  # If no Code provided, name of commodity
    hsType: URIRef  # Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits
    iataCargoAgentCode: URIRef  # IATA accredited cargo agent 7 digit number
    iataCargoAgentLocationIdentifier: (
        URIRef  # IATA CASS cargo agent 4 digit branch number / location identifier
    )
    inPiece: URIRef  # Reference to the Piece this Item or Piece is contained in
    inUnitComposition: URIRef  #
    includedViaPoints: URIRef  # Locations or stations to included in the routing
    incoterms: URIRef  # Standard codes as defined by UNCEFACT and ICC that correspond to international rules for the interpretation of the most commonly used trade terms in different countries. UNECE recommendation n. 5 Incoterms 2.
    insurance: URIRef  # Insurance details
    insuredAmount: URIRef  # Insured amount - amount covered by the insurance policy
    insuredShipments: URIRef  # Reference to the shipments insured
    involvedInActions: URIRef  # References to the Actions the object is involved in
    involvedParties: URIRef  # Information about other Parties involved depending on the context of use
    isotopeId: URIRef  # Id of each radionuclide or for mixtures of radionuclides.
    isotopeName: URIRef  # The name or symbol of each radionuclide or for mixtures of radionuclides, an appropriate general description, or a list of the most restrictive radionuclides.
    isotopes: URIRef  # DgRadioactiveIsotope.
    issuedBy: URIRef  # Name of person (or employee ID) who issued the security status
    issuedForPiece: URIRef  # Reference to the Piece the document was issued for
    issuedForShipment: URIRef  # Reference to the shipment the document was issued for
    issuedForWaybill: URIRef  # Reference to the Waybill object
    issuedOn: URIRef  # Date and time when the security status was issued
    itemQuantity: (
        URIRef  # Quantity of the item when applicable, with associated units of measure
    )
    jobTitle: URIRef  # Job title / position
    knownShipper: URIRef  # Indication if shipper is a Known Shipper as per TSA grant
    lastName: URIRef  # Last name / family name / surname
    latestAcceptanceTime: URIRef  # Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)
    latestArrivalTime: URIRef  # Latest arrival time at destination
    latitude: URIRef  # Location latitude decimal
    legNumber: URIRef  # Leg number
    legacyTemplate: URIRef  # Reference to an ExternalReference holding a legacy template outside of ONE Record, such as a photo or pdf of a checksheet
    length: URIRef  # Length
    lineItemNumber: URIRef  # Number of the line item
    lineItemPackages: URIRef  # References to piece groupings for rating
    loadType: URIRef  # Load type of the shipment or piece (Bulk, ULD, Pallet, Loose)
    loadedMaterials: URIRef  # References to Materials onloaded or offloaded
    loadedPieces: URIRef  # References to Pieces onloaded or offloaded
    loadedUnits: URIRef  # References to LoadingUnits onloaded or offloaded
    loadingActions: URIRef  # References to all actions of type Loading performed for the TransportMovement
    loadingIndicator: URIRef  # ULD height or loading limitation code. Refer CXML Code List 1.47,  e.g. R - ULD Height above 244 centimetres
    loadingPositionIdentifier: (
        URIRef  # Short text stating the loading position in the TransportMeans
    )
    loadingType: URIRef  # Enum stating whether the LoadingAction describes onloading or offloading
    loadingUnit: URIRef  # Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    locationCodes: URIRef  # Location code of airport, freight terminal, seaport, rail station. UN/LOCODE city code (5 letter) or IATA airport code (3 letter)
    locationIndicator: URIRef  # String indicating if the Other Charge Location is Origin (O) or Transit (T) or Destination(D)
    locationName: URIRef  # Full name of the location
    locationType: URIRef  # Location type - e.g. Airport, Freight terminal, Rail station, Seaport, etc
    longText: URIRef  # Long text of the question
    longitude: URIRef  # Location longitude decimal
    lotNumber: URIRef  # Production lot number / reference
    lowDispersibleIndicator: (
        URIRef  # A notation that the material is low dispersible radioactive material.
    )
    manufacturer: URIRef  # Manufacturing company details and contacts
    masterWaybill: URIRef  # Reference to the master Waybill if it is contained in one
    materialModel: URIRef  # Model of the LoadingMaterial if any
    materialType: URIRef  # Type of the LoadingMaterial
    maxSegments: URIRef  # Maximum number of segments for the transportation of the goods. 1 means direct flight
    maxTemperature: URIRef  # Maximum temperature of the range
    maximumQuantity: URIRef  # Maximum quantity
    measurementTimestamp: URIRef  # Timestamp for the measurement
    measurementValue: (
        URIRef  # Information about all non-Geolocation values of the measurement
    )
    measurements: URIRef  # Reference to the Measurements recorded by the Sensor
    methodName: URIRef  # Name of the CO2 calculation method
    methodVersion: URIRef  # Version used for the calculation
    middleName: URIRef  # Middle name/ other name
    minTemperature: URIRef  # Minimum temperature of the range
    minimumQuantity: URIRef  # Minimum quantity
    modeCode: URIRef  # Mode of transport code, refer to UNECE Rec. 19 https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_1cf19e.pdf
    modeQualifier: URIRef  # Pre-Carriage, Main-Carriage or On-Carriage
    modularCheckNumber: URIRef  # The check is a Modular 7 validation on the AWB number, recorded as a boolean.
    movementMilestone: URIRef  # The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.
    movementTimeType: URIRef  # The type of time can be Actual, Estimated ot Scheduled
    movementTimes: URIRef  # Information about times related to the movement (milestone list to be defined)
    movementTimestamp: URIRef  # Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.
    name: URIRef  # Human-understandable name of object depending on the context
    nbCorrections: URIRef  # Number of corrections to CASS records
    netWeightMeasure: URIRef  # The total net weight of dangerous goods transported of this line item. For air transport the value must be the volume or mass in each package.
    note: (
        URIRef  # Free text for customs remarks, not used in OCI Composition Rules Table
    )
    numberOfDoors: URIRef  # Number of doors
    numberOfFittings: URIRef  # Number of fittings
    numberOfNets: URIRef  # Number of nets
    numberOfStraps: URIRef  # Number of straps
    numericalValue: URIRef  # Numerical value
    nvdForCarriage: URIRef  # When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE
    nvdForCustoms: URIRef  # When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE
    ociLineNumber: URIRef  # Integer holding the oci line number when upcasting multi-line oci structures from CIMP/CXML
    odlnCode: URIRef  # Contains two designator codes of ODLN or Operational Damage Limit Notices. ODLN code is used to define type of damage after visually check the serviceability of ULDs section 7, Standard Specifications 4/3 or 4/4 in ULD Regulations
    ofProduct: URIRef  # Reference to the Product describing the Item
    ofShipment: URIRef  # Reference to the Shipment the Piece is assigned to
    offerValidFrom: URIRef  # Date and time of beginning of offer validity
    offerValidTo: URIRef  # Date and time of end of offer validity
    onTransportMeans: (
        URIRef  # Reference to the TransportMeans that is being onloaded or offloaded
    )
    onsiteActions: URIRef  # References to the Actions happening at the Location
    operatedTransportMovement: (
        URIRef  # Transport Movement on which the Transport Means is used
    )
    operatingParties: URIRef  # Information about the parties operating this TransportMovement, for example pilot and co-pilot; can also refer to organizations through Party
    operatingTransportMeans: (
        URIRef  # Reference to the TransportMeans operating the TransportMovement
    )
    originReferencePermitDateTime: URIRef  # Issuing date for Origin reference permit or re-export reference Certificate (box 12)
    originReferencePermitId: URIRef  # identifier of Origin reference permit or re-export reference Certificate (box 12/12a)
    originReferencePermitTypeCode: URIRef  # Document type code of origin reference permit or re-export reference Certificate (box 12/12a)
    originTradeCountry: URIRef  # country of origin (box 12). Refer ISO 3166-2
    originator: URIRef  # Document originator details and contacts
    otherCharacteristics: URIRef  # Characteristics of the product
    otherChargeAmount: URIRef  # Other Charge amount
    otherChargeCode: URIRef  # Refer to CargoXML Code List 1.2 for Other Charges
    otherCharges: URIRef  # Information about Other Charges applying to this Waybill
    otherChargesIndicator: URIRef  # Indicator whether the payment of Other Charges is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 15a/15b from AWB
    otherCustomsInformation: (
        URIRef  # Supplementary Customs, Security and Regulatory Control Information
    )
    otherIdentifierType: URIRef  # Identifier type or description
    otherIdentifiers: (
        URIRef  # Details about any other identifier, depending on the context of use
    )
    otherRegulatedEntities: URIRef  # Any other regulated entity that accepts custody of the cargo and accepts the security status originally issued
    otherScreeningMethods: URIRef  # Other methods used to secure the cargo
    overpackCriticalitySafetyIndexNumeric: URIRef  # Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    overpackIndicator: URIRef  # Overpack indicator
    overpackT1: URIRef  # A single number assigned to a package, overpack or freight container to provide control over radiation exposure.
    overpackTypeCode: URIRef  # Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations
    ownerCode: URIRef  # Owner code of the ULD in aa, an or na format - owner can be an airline or leasing company
    owningOrganization: URIRef  # Reference to the Organization for which the RegulatedEntity information is valid
    packageGrossWeight: (
        URIRef  # Information about the total weight of a grouping of pieces
    )
    packageMarkCoded: URIRef  # Reference identifying how the package is marked. Field is hardcode to "SSCC-18", "UPC" or "Other"
    packageSlac: URIRef  # Integer holding the total slac of a grouping of pieces
    packageVolume: URIRef  # Information about the total volume of a grouping of pieces
    packagedeIdentifier: URIRef  # SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.
    packagingDangerLevelCode: (
        URIRef  # Packing group, If used must reference I, II or III
    )
    packagingType: URIRef  # Packaging details
    packingInstructionNumber: URIRef  # The packing instruction number applicable to the UN number / proper shipping name entry. A three-numeric value which may be preceded by the letter Y.  Mandatory field for air transport (Air)
    parentOrganization: URIRef  # Reference to the parent Organization
    partOfIotDevice: URIRef  # Reference to the IoT Device to which the sensor is linked
    partialEventIndicator: URIRef  # Boolean indicating that the LogisticsEvent is only applicable for parts of the LogisticObject it was recorded for, for example for some Pieces of a Shipment
    partyDetails: URIRef  # Reference to the Agent described by the role of the Party
    partyRole: URIRef  # Role fo the Company in the context. Can refer to Code List 1.36 in the CXML Toolkit
    passed: URIRef  # Boolean indicating whether the Check was passed
    performedAt: URIRef  # Reference to the Location the Action was performed at
    permitTypeCode: URIRef  # Code specifying the document name. (box 1)
    permitTypeOtherDescription: URIRef  # Description if TypeCode is Other (box 1)
    physicalChemicalForm: (
        URIRef  # A description of the physical and chemical form of the material.
    )
    pieceCountForRate: (
        URIRef  # Number of pieces for which the rate description details apply
    )
    pieceGroupCount: URIRef  # Number of pieces in the piece group
    pieceGroupGrossWeight: URIRef  # Total gross weight of the piece group
    pieceGroupId: URIRef  # Identifier of the piece group, increasing integers
    pieceGroups: URIRef  # Reference to the Piece groups of the shipment
    pieceHeight: URIRef  # Height of a single piece
    pieceLength: URIRef  # Length of a single piece
    pieceReferences: URIRef  # References to Pieces for which a rate applies
    pieceWeight: URIRef  # Weight of a single piece
    pieceWidth: URIRef  # Width of a single piece
    pieces: URIRef  # References to the Pieces that are part of this Shipment
    postOfficeBox: URIRef  # Post Office box number / code
    postalCode: URIRef  # Postal / ZIP code
    preferredTransportId: URIRef  # When part of the Request it refers to the preferred Transport ID from the customer. When part of the BookingOption (offer or actual booking) it refers to the expected Transport ID or flight
    prefix: URIRef  # IATA three-numeric airline prefix number
    price: URIRef  # Price of the Booking (if different from the offer)
    priceReferenceId: URIRef  # Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    priceSpecification: (
        URIRef  # Specification of the price e.g. Street, Group, Spot, etc.
    )
    productCode: URIRef  # Carrier's product code
    productDescription: URIRef  # Carrier's product description
    productionCountry: URIRef  # Production country details. Refer ISO 3166-2
    productionCountryForRate: URIRef  # Production country for the rate described by this Line Item. Refer ISO 3166-2
    productionDate: URIRef  # Production date
    properShippingName: URIRef  # The name used to describe the particular article or substance as shown in the UN Model Regulations Dangerous Goods List
    qValueNumeric: URIRef  # Most instances of all packed in one will require the addition of the Q value which  1. Applies to air transport only. (Air)
    quantity: URIRef  # Quantity for the charge if applicable
    quantityAnimals: URIRef  # Quantity including units (box 11)
    quantityForUnitPrice: (
        URIRef  # Product quantity for unit price - e.g. 12 (eggs for one USD 1)
    )
    question: URIRef  # Reference to the Question the Answer is for
    questionNumber: URIRef  # Number of the Question within the template (alphanumeric)
    questionSection: URIRef  # Section of the CheckTemplate this Question is part of
    questions: URIRef  # References to all Questions that are part of this template
    ranges: URIRef  # Reference to the ranges
    rateCharge: URIRef  # TACT Rate for rate description details
    rateClassCode: (
        URIRef  # Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    )
    rateClassCodeBasic: URIRef  # Rate Surcharge/Reduction - Basic Rate Class Code
    rateGrossWeight: (
        URIRef  # Information about the total gross weight considered for a rate
    )
    ratePercentage: URIRef  # Rate Surcharge/Reduction - Percentage of  red. / surcharge
    rateSlac: URIRef  # Integer holding the total slac considered for a rate
    rateVolume: URIRef  # Information about the total volume considered for a rate
    ratings: URIRef  # Rating used for pricing
    rcp: URIRef  # IATA 3-letter city code of the rate combination point as defined in TACT
    reasonDescription: URIRef  # String describing the reason for a charge
    reasonsForAdjustments: (
        URIRef  # A free text for user to include a reason for correction
    )
    receivedFrom: URIRef  # Regulated entity that tendered the consignment
    recordedGeolocation: (
        URIRef  # Reference to the Geolocation recorded of the measurement
    )
    recordingActor: URIRef  # Reference to the Actor recording the LogisticsEvent
    recordingOrganization: URIRef  # Organization recording the LogisticsEvent
    referenceForObjects: URIRef  # References to the LogisticsObjects referring to this external reference
    referredBookingOption: URIRef  # Refers to the Booking
    regionCode: URIRef  # Region/ State / Department. Refer ISO 3166-2
    regulatedEntityAcceptor: URIRef  # Information about the accepting regulated entity of the Security Declaration
    regulatedEntityCategory: URIRef  # Category code of the Regulated Entity
    regulatedEntityExpiryDate: URIRef  # Expiry date 4 digits month/year
    regulatedEntityIdentifier: (
        URIRef  # Regulated entity identifier as per IATA e-CSD/CSD Resolution 65
    )
    regulatedEntityIssuer: URIRef  # Regulated entity issuing the Security Declaration
    remarks: URIRef  # Remarks or Supplement Information
    remarksText: URIRef  # Details of the remarks, mandatory
    reportableQuantity: URIRef  # Reportable quantities, To and from the USA only
    requestMatch: URIRef  # Indicates if the Booking Option is a match to the Booking Option Request preferences
    resultOfCheck: URIRef  #
    resultValue: URIRef  # Information about a result Value of any kind of the Check
    salutation: URIRef  # Salutation
    screeningMethods: URIRef  # Screening methods which have been used to secure the cargo PHS – Physical Inspection and/or hand search VCK - Visual check XRY- X-ray equipment EDS - Explosive detection system EDD - Explosive detection dogsETD - Explosive trace detection equipment - particles or vapor CMD - Cargo metal detection AOM - Subjected to any other means: this entry should be followed by free text specifying what other mean was used to secure the cargo
    seal: URIRef  # Seal identifier
    sealNumber: URIRef  # ULD seal number if applicable
    securityDeclarations: URIRef  # Security details of the piece
    securityStampId: URIRef  # Security Stamp ID
    securityStatus: URIRef  # Security status indicator (CXML 1.13) - e.g. SPX- Cargo Secure for Passenger and All-Cargo Aircraft
    sensorType: (
        URIRef  # Type of sensor as described in Interactive Cargo Recommended Practice
    )
    sequenceNumber: URIRef  # Short text to detail sequence number (alphanumeric)
    serialNumber: URIRef  # Serial number that allows to uniquely identify the object
    servedActivity: URIRef  # Reference to the Activity the Action was performed for
    servedServices: URIRef  # Reference to Services this Activity is executed for
    serviceCode: URIRef  # One letter service code as per bullet point 18.4 - data element 22Z from AWB
    serviceForWaybills: URIRef  # Reference to the Waybills this service is to be performed for. To be used if a service is to be performed for a specific shipment or set of
    serviceLevelCode: URIRef  # Service level code
    serviceProvider: URIRef  # Reference to the Party providing the service
    serviceRequestor: URIRef  # Reference to the Party requesting the service
    serviceabilityCode: URIRef  # Designator of serviceability condition e.g. SER or DAM
    shipment: URIRef  # Reference to the Shipment
    shipperDeclarationText: URIRef  # Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)
    shippingInfo: (
        URIRef  # The shipper or its Agent may enter the appropriate optional shipping
    )
    shippingMarks: URIRef  # Shipping marks
    shippingRefNo: URIRef  # Optional shipping reference number if any
    shortName: URIRef  # Short name of the Organization if any
    shortText: URIRef  # Short text of the Question
    signatoryCompany: URIRef  # Signatory company name
    signatoryRole: URIRef  # Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority
    signatureDate: URIRef  # Date and time of the signature
    signatureStatement: URIRef  # Signatory signature authentication text
    signatureTypeCode: URIRef  # Code specifying a type of government action such as inspection, detention, fumigation, security.
    signatures: URIRef  # List of all the signatures of the Epermit (applicant box 4, issuing authority box 6, issuer box 13 and examining authority box 14)
    skeletonIndicator: (
        URIRef  # Indicator whether a logistics object is a skeleton object
    )
    slac: URIRef  # Shipper's Load And Count  ( total contained piece count as provided by shipper)
    slacForRate: URIRef  # Slac used for the rate described by the Line item
    spaceAllocationCode: (
        URIRef  # Current status of the space allocation of the booking segment
    )
    specialConditions: URIRef  # Special conditions (box 5)
    specialFormIndicator: URIRef  # A notation that the material is special form
    specialHandlingCodes: URIRef  # Three-letter special handling code (SPH)
    specialProvisionId: URIRef  # For Air Mode: Special Provision may show a single, double or triple digit number preceded by the letter A, against appropriate entries in the List of Dangerous Goods
    specialServiceRequests: URIRef  # Special service requests
    speciesCommonName: URIRef  # Species common name (box 8)
    speciesScientificName: URIRef  # Species scientific name (box 7)
    specimenDescription: (
        URIRef  # Description of specimens, including age and sex if LA (box 9)
    )
    specimenTypeCode: URIRef  # Description of specimens, CITES type code (box 9)
    stackable: URIRef  # Stackable indicator for the pieces (boolean)
    station: URIRef  # Reference to the station (Airport), mandatory
    stationRemarks: URIRef  # Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    statusBookingOption: URIRef  # Status of the Booking Option
    storagePlaceIdentifier: URIRef  # Short text stating the exact place of storage
    storedObjects: URIRef  # Reference to the Objects being stored in or stored out
    storingActions: (
        URIRef  # References to all StoringActions performed for the Storing Activity
    )
    storingIdentifier: URIRef  # Short text holding the process number if necessary
    storingType: URIRef  # Enum stating whether the StoringAction describes the store-in or the store-out
    streetAddressLines: URIRef  # Street address including street name, street number, building number, apartment etc
    subLocationOf: URIRef  # Reference to the Location this is a Sublocation of
    subLocations: (
        URIRef  # References to Sublocations that describe the Location in more detail
    )
    subOrganization: URIRef  # References to all sub-Organizations
    subTotal: URIRef  # Subtotal of the charge
    subjectCode: URIRef  # Information Identifier. Code identifying a piece of information/entity e.g. "IMP" for import, "EXP" for export, "AGT" for Agent, "ISS" for The Regulated Agent Issuing the Security Status for a Consignment etc. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    supplementaryInfoPrefix: URIRef  # Additional information that may be added in addition to the proper shipping name to more fully describe the goods or to identify a particular condition
    supplementaryInfoSuffix: URIRef  # Additional information that may be added in addition to the proper shipping to more fully describe the goods or to identify a particular condition
    tareWeight: URIRef  # Tare weight of the empty ULD
    targetCountry: URIRef  # Item target country. Refer ISO 3166-2
    taxAmount: URIRef  # Information about taxes
    taxDueAgent: URIRef  # Tax due Agent (VAT/GST on Commission). Total VAT/TAX amount payable by airline to agent
    taxDueAirline: URIRef  # Tax due Airline (as per AWB, or VAT/GST as per invoice). Total VAT/TAX amount payable by agent to airline
    technicalName: URIRef  # This is additional chemical name(s) required for some proper shipping names. When added the technical must be shown in parentheses immediately following the proper shipping name.
    temperatureInstructions: URIRef  # Temperature instructions if a specific range
    temperatureUnit: URIRef  # Preferred unit for temperature
    templatePurpose: URIRef  # Purpose of the template
    text: URIRef  # Text for the Answer
    textualHandlingInstructions: (
        URIRef  # Strings to provide free text handling instructions such as SSR and OSI
    )
    textualPostCode: URIRef  # Postal / ZIP code
    textualValue: URIRef  # Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    timeOfAvailability: (
        URIRef  # Time of availability of the shipment as per CargoIQ definition
    )
    timePreferences: URIRef  # Schedule preferences of the request
    totalDimensions: URIRef  # Dimensions of the whole shipment
    totalGrossWeight: URIRef  # Total gross weight of the whole shipment
    totalTransitTime: (
        URIRef  # Total transit time as per CargoIQ definition, expressed as a duration
    )
    totalVolume: URIRef  # Total volume fo the volume piece group
    totalVolumetricWeight: URIRef  # Volumetric weight of the whole shipment
    transactionPurpose: URIRef  # Purpose of the transaction in free text (box 5a)
    transactionPurposeCode: (
        URIRef  # Code indicating the purpose of the transaction (box 5a)
    )
    transportContractId: URIRef  # Reference to the Air Waybill or other transport contract document (box 15)
    transportContractTypeCode: (
        URIRef  # Code specifying the transport document name (box 15)
    )
    transportIdentifier: URIRef  # Airline flight number, or rail/truck/maritime line id
    transportIndexNumeric: URIRef  # Radioactive Transport-Index value of the package or all packed in one. Conditionally mandatory and applies to categories II-Yellow and III-Yellow only; field only contains the value, if printed, TI must be added as a prefix to the value  to be printed in the Packing Instructions column
    transportLegs: URIRef  # Reference to the Transport Legs of the proposed routing
    transportMeansServiceType: (
        URIRef  # Type of transport means service, e.g. Aircraftor Truck
    )
    transportMeansType: URIRef  # Type of transport means, e.g. 744, RFS
    transportOrganization: URIRef  # Company operating the transport means
    turnable: URIRef  # Turnable indicator for the pieces (boolean)
    typeCode: URIRef  # Packaging type identifier as per UNECE Rec 21 Annex V and VI e.g. 1A - Drum, steel - Packaging material code. Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations
    typicalCo2Coefficient: URIRef  # Required for some CO2 calculations
    typicalFuelConsumption: URIRef  # Typical fuel consumption (e.g. 2 L / 1 nm)
    uldContourCode: URIRef  # Contour code as per IATA ULD Regulation
    uldLoadingIndicator: (
        URIRef  # Indicator related to ULD loading (e.g. Main deck only)
    )
    uldOwnerCode: URIRef  # Information about the ULD owner code described in a ULD specific piece or used for a rate in a Line Item
    uldRateClassType: URIRef  # ULD Rate information - ULD Rate Class Type
    uldReferences: URIRef  # References to ULDs for which the rate applies
    uldSerialNumber: URIRef  # Serial number that allows to uniquely identify the ULD
    uldTareWeightForRate: URIRef  # Information about the ULD tare weight used for the rate described by the Line Item
    uldType: URIRef  # Type of ULD as per IATA ULD Regulation
    uldTypeCode: URIRef  # Standard Unit Load Device type code e.g. AKE - Certified Container - Contoured. Refer to IATA ULD Technical Manual
    unNumber: URIRef  # Reference identifying the United Nations Dangerous Goods serial number assigned within the UN to substances and articles contained in a list of the dangerous goods most commonly carried. e.g. 1189 - Ethylene glycol monomethyl ether acetate
    uniqueIdentifier: URIRef  # Manufacturer's unique product identifier
    unit: URIRef  # Unit of measurement as per MeasurementUnitCode codelist. If the code is not present, create an instance of MeasurementUnitCode based on UNECE Rec. 20 Rev. 17e-2021
    unitBasis: URIRef  # Specific commodity code linked to commodity
    unitPrice: URIRef  # Product price per unit in the base
    unitsPreference: (
        URIRef  # Reference to unit preferences of the request (e.g. kg or cm)
    )
    updateBookingOptionRequests: (
        URIRef  # References to BookingOptionRequests that request to update the Booking
    )
    upid: URIRef  # Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689
    usedInCheck: URIRef  # Reference to the Check the template was used in
    usedTemplate: URIRef  # Reference to the Template used in the Check
    usedToDateQuotaQuantity: URIRef  # total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    validFrom: URIRef  # Validity start date based on usage context
    validUntil: URIRef  # Validity end date (date of expiry) based on usage context
    vatIndicator: URIRef  # Indicate if subject to VAT (boolean)
    vehicleModel: URIRef  # Model or make of the vehicle (e.g. A33-3)
    vehicleRegistration: (
        URIRef  # Vehicle identification - e.g. aircraft registration number
    )
    vehicleSize: URIRef  # Size of the vehicle - free text
    vehicleType: URIRef  # Vehicle or container type. Refer UNECE28, e.g. 4.. - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manual in section ATA/IATA Aircraft Types
    version: URIRef  # Version of the template
    vis_element: URIRef  # Annotation for ontology visualizer. Indicates what part of the ontology the class is a part of (air core ontology, distribution, ...) to colorize accordingly.
    vis_hidden: URIRef  # Annotation for ontology visualizer. Indicates that the link should be invisible in the ontology viewer.
    vis_inverseProperty: URIRef  # Annotation for ontology visualizer. Indicates what is shown as inverse property (edge) in the visualizer.
    vis_level: URIRef  # Annotation for ontology visualizer. Indicates levels of importance to allow for different views.
    volume: URIRef  # Volume
    volumeUnit: URIRef  # Preferred unit for volume
    volumetricWeight: URIRef  # Volumetric weight details
    volumetricWeightForRate: (
        URIRef  # Volumetric weight used for the rate described by this line item
    )
    waybill: URIRef  # Reference to the Waybill of the shipment
    waybillLineItems: (
        URIRef  # Information about rates applying to this Waybill handled as line item
    )
    waybillNumber: URIRef  # House or Master Waybill unique identifier
    waybillPrefix: (
        URIRef  # Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    )
    waybillType: URIRef  # Type of the Waybill: House, Direct or Master
    weight: URIRef  # Weight of the item
    weightUnit: URIRef  # Preferred unit for weight
    weightValuationIndicator: URIRef  # Indicator whether the payment for the Weight/Valuation is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 14a/14b from AWB
    width: URIRef  # Width
