import pytest
from src.tdd.insurance import Insurance

@pytest.fixture
def insurance():
    return Insurance()

def test_insurance_instantiation(insurance):
    assert isinstance(insurance, Insurance) # Basic check an instance is created
