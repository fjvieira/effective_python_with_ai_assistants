from datetime import date
import pytest
from src.unittesting.car_rules import CarRules

@pytest.fixture
def car_rules():
    return CarRules()

def test_car_rules_instantiation(car_rules):
    assert isinstance(car_rules, CarRules)
