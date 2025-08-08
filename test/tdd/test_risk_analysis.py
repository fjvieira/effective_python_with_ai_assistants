import pytest
from src.tdd.risk_analysis import CompromisedIncome, CreditScore, LoanRisk
 
def test_compromised_income_enum():
    assert CompromisedIncome.LESS_THAN_15_PERCENT.value == "LessThan15Percent"
    assert CompromisedIncome.MORE_THAN_15_PERCENT.value == "MoreThan15Percent"
