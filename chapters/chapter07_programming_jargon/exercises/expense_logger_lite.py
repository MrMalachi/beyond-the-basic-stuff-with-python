"""
Expense Logger Lite - A CLI program where a user records expenses.
"""

expenses = []


def input_expense_category():
    """Prompt user for expense category."""
    while True:
        category = input("\nEnter expense category (or 'done'): ").strip().lower()
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
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = amount  # Store first value if not exist.
        else:
            category_totals[category] += amount # Add to existing amount

    return category_totals


def calculate_largest_expense():
    """Calculate the largest expense amount."""
    largest_expense = max(expense["amount"] for expense in expenses)
    return largest_expense


def display_expense_summary(total, categorical_total_expense, largest_expense):
    """Output a neatly formatted display of the user's expenses."""
    print("--- Expense Summary ---")
    print(f"Total Spent: ${total:.2f}")

    print("\nBy Category:")
    for category, amount in categorical_total_expense.items():
        print(f"{category.title()}: ${amount}")

    print("\nLargest Expense:")
    print(f"{largest_expense}")


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
    categorical_total_expense = calculate_category_expenses()
    largest_expense = calculate_largest_expense()
    display_expense_summary(total, categorical_total_expense, largest_expense)


run_expense_logger()



