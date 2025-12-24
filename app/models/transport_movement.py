from typing import List

from app.models.location import Location
from app.models.logistics_activity import LogisticsActivity
from app.models.movement_time import MovementTime
from app.models.party import Party


class TransportMovement(LogisticsActivity):
    arrival_location: Location
    departure_location: Location
    movement_times: List[MovementTime]
    operating_parties: List[Party]
