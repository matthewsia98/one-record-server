from app.models.logistics_agent import LogisticsAgent


class Carrier(LogisticsAgent):
    airlineCode: str
    prefix: str
    name: str
