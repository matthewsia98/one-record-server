from rdflib import URIRef

from app.namespaces import CARGO


class MovementTimeTypeValidator:
    @staticmethod
    def validate(value: URIRef) -> URIRef:
        valid_values = {
            CARGO.ACTUAL,
            CARGO.ESTIMATED,
            CARGO.SCHEDULED,
        }

        if value not in valid_values:
            raise ValueError(
                f"Invalid Movement Time Type: {value}. Must be one of: {[str(v) for v in valid_values]}"
            )

        return value
