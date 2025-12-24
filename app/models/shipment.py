from pydantic import BaseModel

from app.models.common import Graphable


class Shipment(BaseModel, Graphable): ...
