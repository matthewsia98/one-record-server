from rdflib import URIRef

from app.namespaces import API


class TopicTypeValidator:
    @staticmethod
    def validate(value: URIRef) -> URIRef:
        valid_values = {
            API.LOGISTICS_OBJECT_TYPE,
            API.LOGISTICS_OBJECT_IDENTIFIER,
        }

        if value not in valid_values:
            raise ValueError(
                f"Invalid Topic Type: {value}. Must be one of: {[str(v) for v in valid_values]}"
            )

        return value
