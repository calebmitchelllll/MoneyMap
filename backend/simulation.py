# This file handles the growth simulation over time.

def simulate_growth(initial_amount, monthly_contribution, annual_return, years):
    months = years * 12
    monthly_rate = annual_return / 12
    balance = initial_amount
    yearly_values = []

    for month in range(1, months + 1):
        # Grow current balance, then add monthly contribution
        balance = balance * (1 + monthly_rate) + monthly_contribution

        # Save end-of-year values
        if month % 12 == 0:
            yearly_values.append(round(balance, 2))

    return yearly_values


def run_all_simulations(initial_amount, monthly_contribution, years, strategies):
    results = {}

    for name, strategy in strategies.items():
        yearly_values = simulate_growth(
            initial_amount=initial_amount,
            monthly_contribution=monthly_contribution,
            annual_return=strategy["expected_return"],
            years=years
        )

        results[name] = {
            "allocation": {
                "stocks": strategy["stocks"],
                "bonds": strategy["bonds"],
                "cash": strategy["cash"]
            },
            "risk": strategy["risk"],
            "expected_return": strategy["expected_return"],
            "yearly_values": yearly_values,
            "final_value": yearly_values[-1] if yearly_values else initial_amount
        }

    return results