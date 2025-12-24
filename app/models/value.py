from pydantic import BaseModel

from app.models.common import IRI


class Value(BaseModel):
    unit: IRI
    numerical_value: float
