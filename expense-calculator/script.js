// Add a new row to the expense table
function addRow() {
    const tbody = document.getElementById('expense-tbody');
    const row = document.createElement('tr');
    row.innerHTML = `
        <td><input type="text" name="category" required></td>
        <td><input type="number" name="amount" min="0" required></td>
        <td><button type="button" class="remove-btn" onclick="removeRow(this)">Remove</button></td>
    `;
    tbody.appendChild(row);
}

// Remove a row from the expense table
function removeRow(btn) {
    const row = btn.closest('tr');
    row.remove();
}

document.getElementById('add-row-btn').addEventListener('click', addRow);
document.getElementById('calculate-btn').addEventListener('click', calculateExpenses);

function calculateExpenses() {
    const rows = document.querySelectorAll('#expense-tbody tr');
    let expenses = [];
    let total = 0;

    rows.forEach(row => {
        const category = row.querySelector('input[name="category"]').value.trim();
        const amount = parseFloat(row.querySelector('input[name="amount"]').value);
        if (category && !isNaN(amount)) {
            expenses.push({ category, amount });
            total += amount;
        }
    });

    // Calculate average daily expense (assuming 30 days in a month)
    const avgDaily = total / 30;

    // Get top 3 largest expenses
    const top3 = expenses.sort((a, b) => b.amount - a.amount).slice(0, 3);

    // Display results
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <strong>Total Expenses:</strong> $${total.toLocaleString()}<br>
        <strong>Average Daily Expense:</strong> $${avgDaily.toLocaleString(undefined, {maximumFractionDigits: 2})}<br>
        <strong>Top 3 Expenses:</strong>
        <ol>
            ${top3.map(e => `<li>${e.category} ($${e.amount.toLocaleString()})</li>`).join('')}
        </ol>
    `;
} 