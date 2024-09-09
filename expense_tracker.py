# expense_tracker.py

# Step 1: Define a list to store our expenses
expenses = []

# Step 2: Define a function to add an expense
def add_expense(date, description, amount):
    expense = {"date": date, "description": description, "amount": amount}
    expenses.append(expense)

# Step 3: Define a function to view all expenses
def view_expenses():
    for expense in expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")

# Step 4: Define the main function to run the application
def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            add_expense(date, description, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
# expense_tracker.py

# Step 5: Define a function to calculate total expenses
def calculate_total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: {total}")

# Modify the view_expenses function to include total expenses
def view_expenses():
    for expense in expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")
    calculate_total_expenses()
import json

# Step 6: Define functions to save and load data
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved to expenses.json.")

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No saved expenses found.")
def main():
    load_expenses()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save & Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            add_expense(date, description, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses()
            break
        else:
            print("Invalid choice, please try again.")
