import sqlite3

# Initialize the database and populate data
with open('init_db.sql', 'r') as f:
    init_sql = f.read()

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.executescript(init_sql)

# Helper to run a query from file
def run_query(filename):
    with open(filename, 'r') as f:
        sql = f.read()
    c.execute(sql)
    return c.fetchall()

# 1. Total sales for March 2024
march_sales = run_query('total_sales_march.sql')
print(f"Total sales for March 2024: {march_sales[0][0]}")

# 2. Top-spending customer
top_customer = run_query('top_customer.sql')
print(f"Top-spending customer: {top_customer[0][0]} ({top_customer[0][1]})")

# 3. Average order value for last 3 months
avg_order = run_query('avg_order_value_last3months.sql')
print(f"Average order value (last 3 months): {avg_order[0][0]}")

conn.close() 