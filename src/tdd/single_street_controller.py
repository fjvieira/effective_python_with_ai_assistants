from enum import Enum

class SingleStreetController:
    class PedestrianLight(Enum):
        RED = "RED"
        GREEN = "GREEN"

    class TrafficLight(Enum):
        RED = "RED"
        YELLOW = "YELLOW"
        GREEN = "GREEN"
