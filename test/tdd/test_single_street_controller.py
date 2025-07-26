import pytest
from src.tdd.single_street_controller import SingleStreetController

@pytest.fixture
def controller():
    return SingleStreetController()

def test_single_street_controller_instantiation(controller):
    assert isinstance(controller, SingleStreetController)
