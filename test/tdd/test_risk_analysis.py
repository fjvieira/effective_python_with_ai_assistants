import pytest
from src.tdd.risk_analysis import RiskAnalysis

@pytest.fixture
def analysis():
    return RiskAnalysis()

def test_risk_analysis_instantiation(analysis):
    assert isinstance(analysis, RiskAnalysis)
