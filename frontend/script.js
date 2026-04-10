document.getElementById("runBtn").addEventListener("click", () => {
  const data = {
    savings: document.getElementById("savings").value,
    income: document.getElementById("income").value,
    expenses: document.getElementById("expenses").value,
    investment: document.getElementById("investment").value,
    risk: document.getElementById("risk").value,
    timeline: document.getElementById("timeline").value
  };

  document.getElementById("results").textContent =
    JSON.stringify(data, null, 2);
});