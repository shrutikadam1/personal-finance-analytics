import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense_tracker"
)

query = """
SELECT e.date, e.amount, e.payment_method, e.note, c.name as category
FROM expense e
JOIN categories c ON e.category_id = c.id
ORDER BY e.date
"""

df = pd.read_sql(query, connection)
df.to_csv('all_expenses.csv', index=False)
print(f"Exported {len(df)} expenses!")