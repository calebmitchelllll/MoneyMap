# This file creates the investment strategy options
# and checks emergency fund status.

def generate_strategies(savings, monthly_income, monthly_expenses, monthly_investment, risk_tolerance):
    # 6-month emergency fund target
    emergency_fund_target = monthly_expenses * 6

    # How far below target the user is
    emergency_fund_gap = max(0, emergency_fund_target - savings)

    # Basic preset strategies
    strategies = {
        "conservative": {
            "stocks": 0.30,
            "bonds": 0.40,
            "cash": 0.30,
            "expected_return": 0.04,
            "risk": "Low"
        },
        "balanced": {
            "stocks": 0.50,
            "bonds": 0.30,
            "cash": 0.20,
            "expected_return": 0.06,
            "risk": "Medium"
        },
        "growth": {
            "stocks": 0.75,
            "bonds": 0.15,
            "cash": 0.10,
            "expected_return": 0.08,
            "risk": "High"
        }
    }

    return {
        "emergency_fund_target": emergency_fund_target,
        "emergency_fund_gap": emergency_fund_gap,
        "strategies": strategies
    }
