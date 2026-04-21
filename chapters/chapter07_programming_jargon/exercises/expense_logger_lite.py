"""
Expense Logger Lite - A CLI program where a user records expenses.
"""

expenses = []


def input_expense_category():
    """Prompt user for expense category."""
    while True:
        category = input("\nEnter expense category (or 'done'): ").strip()
        if category == "":
            print("\nYou must enter an expense category...")
        else:
            return category


def input_expense_amount():
    """Prompt user to enter the expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: $").strip())
        except ValueError:
            print("\nThe expense amount must be a whole or mixed number...")
        else:
            return amount


def input_expense_description():
    """Prompt user to enter a short description of the expense."""
    while True:
        description = input("Enter description: ").strip()

        if description == "":
            print("\nYou must enter a description of the expense...")
        else:
            return description


def calculate_total_expenses():
    """Calculate the total price of expenses entered."""
    total = 0
    total += (expense["amount"] for expense in expenses)
    return total


def calculate_category_expenses():
    """Calculate the total expenses for each category."""



def display_expense_summary(total, category_totals=0):
    """Output a neatly formatted display of the user's expenses."""
    print("--- Expense Summary ---")
    print(f"Total Spent: ${total}")

    print("By Category:")



def run_expense_logger():
    """Orchestrator function."""
    while True:
        category = input_expense_category()
        if category.lower() == "done":
            break

        amount = input_expense_amount()
        description = input_expense_description()
        expenses.append({
            "category": category, "amount": amount, "description": description
        })

    total = calculate_total_expenses()
    display_expense_summary(total)


run_expense_logger()



