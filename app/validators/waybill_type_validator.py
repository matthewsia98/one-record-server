from rdflib import URIRef

from app.namespaces import CARGO


class WaybillTypeValidator:
    @staticmethod
    def validate(value: URIRef) -> URIRef:
        valid_values = [CARGO.DIRECT, CARGO.HOUSE, CARGO.MASTER]

        if value not in valid_values:
            raise ValueError(
                f"Invalid Waybill Type: {value}. Must be one of: {[str(v) for v in valid_values]}"
            )

        return value
