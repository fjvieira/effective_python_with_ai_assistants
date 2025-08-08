from enum import Enum
from datetime import datetime


class CarRules:
    class FuelType(Enum):
        GASOLINE = "GASOLINE"
        ALCOHOL = "ALCOHOL"

    class TripType(Enum):
        CITY = "CITY"
        HIGHWAY = "HIGHWAY"

    def should_schedule_review(
            self, current_odometer: int, last_revision_odometer: int,
            last_revision_date: datetime) -> bool:
        kilometers = current_odometer - last_revision_odometer

        kilometers_check = kilometers >= 10000

        twelve_months_later = last_revision_date.replace(
            year=last_revision_date.year + 1)
        months_check = twelve_months_later <= datetime.today()

        return months_check or kilometers_check

    def calculate_true_efficiency(
            self, distance_traveled: float, fuel_consumed: float, fuel_type: FuelType,
            trip_type: TripType) -> float:
        if fuel_consumed <= 0:
            raise ValueError("Fuel consumed must be greater than zero.")

        base_efficiency = self._get_base_efficiency(fuel_type, trip_type)

        if base_efficiency == 0:
            return float('inf') if distance_traveled > 0 else 0.0

        actual_efficiency = distance_traveled / fuel_consumed
        return actual_efficiency / base_efficiency

    def calculate_autonomy(self, fuel_in_tank: float, fuel_type: FuelType,
                           trip_type: TripType) -> float:
        efficiency = self._get_base_efficiency(fuel_type, trip_type)
        return fuel_in_tank * efficiency

    def _get_base_efficiency(self, fuel_type: FuelType, trip_type: TripType) -> float:
        if fuel_type == CarRules.FuelType.GASOLINE:
            return 12 if trip_type == CarRules.TripType.CITY else 15
        elif fuel_type == CarRules.FuelType.ALCOHOL:
            return 8 if trip_type == CarRules.TripType.CITY else 10
        return 0.0
