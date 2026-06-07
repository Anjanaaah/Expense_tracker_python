import sqlite3

# Create database and table
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()


# Add Expense
def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses(amount, category, description, date)
        VALUES (?, ?, ?, ?)
        """,
        (amount, category, description, date)
    )

    conn.commit()
    conn.close()

    print("Expense Added Successfully!")


# View Expenses
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    print("\nExpenses List")
    print("-" * 50)

    for row in rows:
        print(row)

    conn.close()


# Delete Expense
def delete_expense():
    expense_id = int(input("Enter Expense ID to Delete: "))

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    print("Expense Deleted Successfully!")


# Update Expense
def update_expense():
    expense_id = int(input("Enter Expense ID: "))
    new_amount = float(input("Enter New Amount: "))

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET amount = ?
        WHERE id = ?
        """,
        (new_amount, expense_id)
    )

    conn.commit()
    conn.close()

    print("Expense Updated Successfully!")


# Total Expense
def total_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    print("\nTotal Expense =", total)

    conn.close()


# Main Menu
while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Total Expense")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        total_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")