from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class API(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 20:10:56.183817
    """

    _NS = Namespace("https://onerecord.iata.org/ns/api#")

    _fail = True

    ACCESS_DELEGATION_REQUEST_ACCEPTED: URIRef  #
    ACCESS_DELEGATION_REQUEST_FAILED: URIRef  #
    ACCESS_DELEGATION_REQUEST_PENDING: URIRef  #
    ACCESS_DELEGATION_REQUEST_REJECTED: URIRef  #
    ACCESS_DELEGATION_REQUEST_REVOKED: URIRef  #
    ADD: URIRef  # Defines a :PatchOperation to be an operation that adds new triples.
    AccessDelegation: (
        URIRef  # Access to a Logistics Object delegated to an Organization
    )
    AccessDelegationRequest: URIRef  # Delegation Request to 3rd parties
    ActionRequest: URIRef  # Superclass for all kinds of requests (i.e someone requsted something (e.g. subscription, access, etc.) at a publisher/holder of a logistics object)
    AuditTrail: URIRef  # Audit trail of a Logistics Object
    CHANGE_REQUEST_ACCEPTED: URIRef  # :EventType for accepted :ChangeRequests
    CHANGE_REQUEST_FAILED: URIRef  # :EventType for failed :ChangeRequests.
    CHANGE_REQUEST_PENDING: URIRef  # :EventType for pending :ChangeRequests.
    CHANGE_REQUEST_REJECTED: URIRef  #
    CHANGE_REQUEST_REVOKED: URIRef  #
    Change: URIRef  #
    ChangeRequest: URIRef  # Change Request containing updates on a Logistics Object
    Collection: URIRef  # Used as response of endpoints returning a collection of more than one graph, i.e. more than one not linked subjects.
    DELETE: URIRef  #
    Error: URIRef  # Error model
    ErrorDetail: URIRef  # Error details that belong to an error
    GET_LOGISTICS_EVENT: URIRef  # :Permission to get a :LogisticsEvent
    GET_LOGISTICS_OBJECT: URIRef  # :Permission to get a :LogisticsObject
    LOGISTICS_EVENT_RECEIVED: URIRef  #
    LOGISTICS_OBJECT_ACCESS_GRANTED: URIRef  #
    LOGISTICS_OBJECT_AVAILABLE: URIRef  #
    LOGISTICS_OBJECT_CREATED: URIRef  #
    LOGISTICS_OBJECT_IDENTIFIER: URIRef  #
    LOGISTICS_OBJECT_TYPE: URIRef  #
    LOGISTICS_OBJECT_UPDATED: URIRef  #
    Notification: URIRef  # Notification sent by the publisher to the subscriber
    NotificationEventType: URIRef  #
    Operation: URIRef  # Operation Request contained in the PATCH body
    OperationObject: URIRef  # Object to modify in the PATCH request
    PATCH_LOGISTICS_OBJECT: URIRef  #
    POST_LOGISTICS_EVENT: URIRef  # :Permission to add a logistics event.
    PatchOperation: URIRef  #
    Permission: URIRef  #
    REQUEST_ACCEPTED: URIRef  #
    REQUEST_ACKNOWLEDGED: URIRef  #
    REQUEST_FAILED: URIRef  #
    REQUEST_PENDING: URIRef  #
    REQUEST_REJECTED: URIRef  #
    REQUEST_REVOKED: URIRef  #
    RequestStatus: URIRef  #
    SUBSCRIPTION_REQUEST_ACCEPTED: URIRef  #
    SUBSCRIPTION_REQUEST_FAILED: URIRef  #
    SUBSCRIPTION_REQUEST_PENDING: URIRef  #
    SUBSCRIPTION_REQUEST_REJECTED: URIRef  #
    SUBSCRIPTION_REQUEST_REVOKED: URIRef  #
    ServerInformation: URIRef  # Information about the ONE Record server
    Subscription: URIRef  # Subscription information sent to the publisher
    SubscriptionEventType: URIRef  #
    SubscriptionRequest: URIRef  # SubscriptionRequest initiated by subscribers to publisher (data holder) for themselves or for a third party subscriber.
    TopicType: URIRef  #
    VERIFICATION_REQUEST_ACKNOWLEDGED: URIRef  #
    VERIFICATION_REQUEST_FAILED: URIRef  #
    VERIFICATION_REQUEST_PENDING: URIRef  #
    VERIFICATION_REQUEST_REJECTED: URIRef  #
    VERIFICATION_REQUEST_REVOKED: URIRef  #
    Verification: URIRef  #
    VerificationRequest: URIRef  #
    expiresAt: URIRef  # Expiry date as date time of the subscription information that supports caching but does not require the ONE Record client to store the datetime when the Subscription object was received; if not given: the information does not expire
    hasAccessDelegation: URIRef  #
    hasActionRequest: URIRef  # Link any type of Action Request
    hasChange: URIRef  # Contains submitted Change object
    hasChangeRequest: (
        URIRef  # Recorded change requests in the Audit Trail of a Logistics Object
    )
    hasChangedProperty: URIRef  # List of all changed properties as URIRefs after a ChangeRequest was successfully applied, e.g. [https://onerecord.iata.org/ns/cargo#hasVolumetricWeight, https://onerecord.iata.org/ns/cargo/#hasGoodsDescription]
    hasCode: URIRef  # Error code is a numeric or alphanumeric code that can be used to determine the source of the error and why it occured.
    hasContentType: URIRef  # Content types that the subscriber wants to receive in the notifications, e.g. application/ld+json
    hasDataHolder: URIRef  # The data holder of the servers data.
    hasDatatype: URIRef  # Data type of the field to update, must be a valid URI, e.g. http://www.w3.org/2001/XMLSchema#int
    hasDescription: URIRef  # Reason for the request (optional)
    hasError: URIRef  # Error object(s) if the processing was not successful
    hasErrorDetail: URIRef  # Error details
    hasEventType: URIRef  #
    hasItem: URIRef  # Item that is contained in a collection
    hasLatestRevision: (
        URIRef  # Latest revision of the Logistics Object. Starting with revision 0
    )
    hasLogisticsEvent: URIRef  # A reference to a cargo LogisticsEvent
    hasLogisticsObject: URIRef  # A reference to a cargo:LogisticsObject.
    hasLogisticsObjectType: URIRef  # The type of cargo:LogisticsObject in the notification e.g. https://onerecord.iata.org/ns/cargo#Piece
    hasMessage: URIRef  # Message that describes the error
    hasOperation: URIRef  # Operation(s) to apply as PATCH on a Logistics Object
    hasPermission: URIRef  #
    hasProperty: URIRef  # Property of the object for which the error applies in URIRef format, i.e. https://onerecord.iata.org/ns/cargo#hasVolumetricWeight
    hasRequestStatus: URIRef  #
    hasResource: URIRef  # URI of the object where the error occurred
    hasRevision: URIRef  # Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    hasServerEndpoint: URIRef  # ONE Record API endpoint
    hasSubscriber: URIRef  #
    hasSubscription: URIRef  # Link to the requestors Subscription object with all subscription information
    hasSupportedApiVersion: URIRef  # Supported ONE Record API versions by the server, MUST include at least one supported version.
    hasSupportedContentType: URIRef  # Supported content types of the server, MUST contain at least application/ld+json
    hasSupportedEncoding: URIRef  # Optional list of supported encodings of the ONE Record server, e.g. gzip
    hasSupportedLanguage: URIRef  # Supported languages of the ONE Record API, minimum is en-US (American English)
    hasSupportedOntology: (
        URIRef  # Supported ontologies on the server, MUST be non-versioned URIRefs
    )
    hasSupportedOntologyVersion: (
        URIRef  # Supported ontology versions on the server, MUST be versioned URIRefs
    )
    hasTitle: URIRef  # Short summary of the error
    hasTopic: URIRef  # The Logistics Object type or specific Logistics Object to which the subscription belongs to e.g. https://onerecord.iata.org/Piece or https://1r.example.com/7f01363f-0c6a-4414-be48-d3692e219b91
    hasTopicType: URIRef  #
    hasTotalItems: URIRef  # The number of total items contained in a collection
    hasValue: URIRef  # Updated value for the field
    hasVerification: URIRef  # Links to the Verification class
    hasVerificationRequest: URIRef  # Link to the Verification Request
    includeSubscriptionEventType: URIRef  # An array used to indicate the specific types of notifications that the subscriber desires to receive from the publisher. The subscriber is required to specify their preferences on a per-type basis
    isRequestedAt: URIRef  # Datetime when the request was created
    isRequestedBy: URIRef  # Organization Identifier that represents the Organization that has requested the action
    isRequestedFor: URIRef  #
    isRevokedAt: URIRef  # The datetime when the action request was revoked.
    isRevokedBy: URIRef  #
    isTriggeredBy: URIRef  # Optional URI to the ChangeRequest that triggered a Notification if the eventType is one of CHANGE_REQUEST_ACCEPTED, CHANGE_REQUEST_REJECT, or CHANGE_REQUEST_FAILED
    notifyRequestStatusChange: URIRef  # Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    o: URIRef  #
    op: URIRef  #
    p: URIRef  # Operations objects must have exactly one p, predicate, member. The value of this member must be an URI, e.g. https://onerecord.iata.org/ns/cargo#hasGoodsDescription
    s: URIRef  # Operation objects MUST have exactly one "s", subject, member. The value of this member MUST be one of URIRef or blank node.
    sendLogisticsObjectBody: URIRef  # Flag specifying if the publisher should send the whole logistics object or not in the notification object
