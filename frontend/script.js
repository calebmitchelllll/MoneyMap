document.getElementById("runBtn").addEventListener("click", async () => {
  const data = {
    savings: Number(document.getElementById("savings").value),
    income: Number(document.getElementById("income").value),
    expenses: Number(document.getElementById("expenses").value),
    investment: Number(document.getElementById("investment").value),
    risk: document.getElementById("risk").value,
    timeline: Number(document.getElementById("timeline").value)
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/simulate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("results").textContent =
      JSON.stringify(result, null, 2);
  } catch (error) {
    document.getElementById("results").textContent =
      "Error connecting to backend: " + error.message;
  }
});