# AI Tasks Project

This project contains three independent tasks:

1. **Monthly Expense Calculator (Web App)**
2. **API Testing: Identifying Defects in Product Data**
3. **SQL Queries: Analyzing a Database Online**

---

## 1. Monthly Expense Calculator (Web App)

**Directory:** `expense-calculator/`

### How to Run

1. Open a terminal and navigate to the `expense-calculator` directory:
    ```bash
    cd expense-calculator
    ```
2. Start a local server:
    ```bash
    bash serve.sh
    ```
3. Open your browser and go to [http://localhost:8000](http://localhost:8000)
4. Use the web interface to add expenses and calculate indicators.

---

## 2. API Testing: Identifying Defects in Product Data

**Directory:** `api-testing/`

### How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the test script:
    ```bash
    python test_fakestoreapi.py
    ```
3. The script will fetch product data from the public API, check for defects, and print any issues found.

---

## 3. SQL Queries: Analyzing a Database Online

**Directory:** `sql-queries/`

### How to Run

1. Make sure you have Python (with sqlite3, included by default).
2. Navigate to the `sql-queries` directory:
    ```bash
    cd sql-queries
    ```
3. Run the Python script to initialize the database and execute the queries:
    ```bash
    python run_queries.py
    ```
4. The script will print:
    - Total sales for March 2024
    - The top-spending customer
    - The average order value for the last three months

---
