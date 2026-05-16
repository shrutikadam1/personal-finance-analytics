import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense_tracker"

)

print("Connected Successfully!")

cursor = connection.cursor()

def view_all_expenses():
    cursor.execute("SELECT * FROM expense")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[3]}, Payment: {row[4]}, Note: {row[5]}")


def add_expense(date, time, amount, payment_method, note, category_id):
    query = """INSERT INTO expense (date, time, amount, payment_method, note, category_id) VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (date, time, amount, payment_method, note, category_id)
    cursor.execute(query, values)
    connection.commit()
    print("Expense added successfully!")


def delete_expense(expense_id):
    query = "DELETE FROM expense WHERE id = %s"
    cursor.execute(query, (expense_id,))
    connection.commit()
    print("Expense deleted successfully!")

def view_categories():
    cursor.execute("SELECT * FROM categories")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}")

def update_expense(expense_id, new_amount, new_note):
    query = "UPDATE expense SET amount =%s, note = %s WHERE id = %s"
    values = (new_amount, new_note, expense_id)
    cursor.execute(query, values)
    connection.commit()
    print("Expense updated successfully!")

def view_by_category(category_id):
    query = "SELECT * FROM expense e JOIN categories c ON e.category_id = c.id WHERE c.id = %s"
    cursor.execute(query, (category_id,))
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[3]}, Payment: {row[4]}, Note: {row[5]}")

def spending_summary():
    query = "SELECT c.name, SUM(e.amount) FROM expense e JOIN categories c ON e.category_id = c.id GROUP BY c.name"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Spending Summary by Category:")
    for row in results:
        print(f"Category: {row[0]}, Total Spent: ${row[1]}")



#menu for user interaction
while True:
    print("\nExpense Tracker Menu:")
    print("1. View All Expenses")
    print("2. Add New Expense")
    print("3. Delete Expense")
    print("4. Exit")
    print("5. Update Expense")
    print("6. View Expenses by Category")
    print("7. View Spending Summary by Category")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        view_all_expenses()
    elif choice == '2':
        view_categories()
        date = input("Enter the date (YYYY-MM-DD): ")
        time = input("Enter the time (HH:MM:SS): ")
        amount = float(input("Enter the amount: $"))
        payment_method = input("Enter the payment method: ")
        note = input("Enter a note for this expense: ")
        category_id = int(input("Enter the category ID: "))
        add_expense(date, time, amount, payment_method, note, category_id)
    elif choice == '3':
        expense_id = int(input("Enter the ID of the expense to delete: "))
        delete_expense(expense_id)
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        break
    elif choice == '5':
        expense_id = int(input("Enter the ID of the expense to update: "))
        new_amount = float(input("Enter the new amount: $"))
        new_note = input("Enter the new note: ")
        update_expense(expense_id, new_amount, new_note)
    elif choice == '6':
        view_categories()
        category_id = int(input("Enter the category ID: "))
        view_by_category(category_id)
    elif choice == '7':
        spending_summary()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")