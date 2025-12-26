from rdflib import URIRef

from app.namespaces import CODELISTS


class ParticipantIdentifierValidator:
    @staticmethod
    def validate(value: URIRef) -> URIRef:
        valid_values = dir(CODELISTS.ParticipantIdentifier)

        if value not in valid_values:
            raise ValueError(
                f"Invalid Participant Identifier: {value}. Must be one of: {valid_values}"
            )

        return value
