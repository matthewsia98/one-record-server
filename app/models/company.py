from app.models.location import Location
from app.models.logistics_agent import LogisticsAgent


class Company(LogisticsAgent):
    based_at_location: Location
    name: str
