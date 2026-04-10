# Main FastAPI backend file

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

from financial_logic import generate_strategies
from simulation import run_all_simulations

# Let Python find the ai folder one level above backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ai.ai_summary import generate_summary

app = FastAPI()

# Allow the frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This matches your frontend field names exactly
class UserInput(BaseModel):
    savings: float
    income: float
    expenses: float
    investment: float
    risk: str
    timeline: int

@app.get("/")
def root():
    return {"message": "WealthSim backend is running"}

@app.post("/simulate")
def simulate(user_input: UserInput):
    # Build strategy info and emergency fund info
    financial_data = generate_strategies(
        savings=user_input.savings,
        monthly_income=user_input.income,
        monthly_expenses=user_input.expenses,
        monthly_investment=user_input.investment,
        risk_tolerance=user_input.risk
    )

    # Run the simulation using monthly investment as the recurring contribution
    simulation_results = run_all_simulations(
        initial_amount=user_input.savings,
        monthly_contribution=user_input.investment,
        years=user_input.timeline,
        strategies=financial_data["strategies"]
    )

    # Generate summary text
    summary = generate_summary(
        user_data=user_input.model_dump(),
        strategy_results=simulation_results,
        emergency_fund_gap=financial_data["emergency_fund_gap"]
    )

    return {
        "emergency_fund_target": financial_data["emergency_fund_target"],
        "emergency_fund_gap": financial_data["emergency_fund_gap"],
        "strategy_results": simulation_results,
        "summary": summary
    }
