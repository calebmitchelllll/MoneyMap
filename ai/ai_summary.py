# This is a placeholder summary generator.
# Later, this can be replaced by a real Claude API call.

def generate_summary(user_data, strategy_results, emergency_fund_gap):
    risk_tolerance = user_data["risk"]

    if emergency_fund_gap > 0:
        warning = (
            f"You are about ${emergency_fund_gap:.2f} below a 6-month emergency fund target, "
            "so building more savings first may be important."
        )
    else:
        warning = "You appear to have met a 6-month emergency fund target."

    if risk_tolerance == "low":
        fit = "The conservative strategy may fit best because it prioritizes stability."
    elif risk_tolerance == "medium":
        fit = "The balanced strategy may fit best because it mixes growth and stability."
    else:
        fit = "The growth strategy may fit best if you are comfortable with more volatility."

    conservative_value = strategy_results["conservative"]["final_value"]
    balanced_value = strategy_results["balanced"]["final_value"]
    growth_value = strategy_results["growth"]["final_value"]

    comparison = (
        f"Projected final values are approximately "
        f"${conservative_value:.2f} for conservative, "
        f"${balanced_value:.2f} for balanced, and "
        f"${growth_value:.2f} for growth."
    )

    return {
        "warning": warning,
        "fit_summary": fit,
        "comparison": comparison
    }