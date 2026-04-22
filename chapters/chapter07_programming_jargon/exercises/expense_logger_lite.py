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
            amount = round(float(input("Enter amount: $").strip()))
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
    total = sum(expense["amount"] for expense in expenses)
    return total


def calculate_category_expenses():
    """Calculate the total expenses for each category."""
    category = expenses[0]["category"]
    amount = expenses[0]["amount"]
    categorical_expense_total = sum(amount for category in expenses)
    return categorical_expense_total


def display_expense_summary(total, category_expense_total):
    """Output a neatly formatted display of the user's expenses."""
    print("--- Expense Summary ---")
    print(f"Total Spent: ${total:.2f}")

    print("\nBy Category:")
    print(f"{category_expense_total}")


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
    categorical_expense_total = calculate_category_expenses()
    display_expense_summary(total, categorical_expense_total)


run_expense_logger()



