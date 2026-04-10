from flask import Flask, request, jsonify
from flask_cors import CORS

from financial_logic import build_financial_plan
from simulation import run_simulation
from ai_summary import generate_summary

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "WealthSim backend is running"})


@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400


        # Example data flow.
        plan = build_financial_plan(data)
        simulation_results = run_simulation(plan)
        summary = generate_summary(plan, simulation_results)

        return jsonify({
            "plan": plan,
            "simulation": simulation_results,
            "summary": summary
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)