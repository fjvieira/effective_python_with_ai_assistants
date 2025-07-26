from enum import Enum

class LoanRisk(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class CreditScore(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class CompromisedIncome(Enum):
    LESS_THAN_15_PERCENT = "LessThan15Percent"
    MORE_THAN_15_PERCENT = "MoreThan15Percent"

