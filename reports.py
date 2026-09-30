def calculate_totals(transactions):
    income = 0
    expense = 0

    for item in transactions:
        if item["type"] == "income":
            income += item["amount"]
        elif item["type"] == "expense":
            expense += item["amount"]

    balance = income - expense
    return income, expense, balance


def category_totals(transactions):
    result = {}

    for item in transactions:
        if item["type"] != "expense":
            continue

        category = item["category"]

        if category in result:
            result[category] += item["amount"]
        else:
            result[category] = item["amount"]

    return result


def highest_expense(transactions):
    expenses = [
        item for item in transactions
        if item["type"] == "expense"
    ]

    if not expenses:
        return None

    return max(expenses, key=lambda item: item["amount"])
