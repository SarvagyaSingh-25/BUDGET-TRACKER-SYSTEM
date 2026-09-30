from datetime import datetime
from storage import load_data, save_data
from reports import calculate_totals, category_totals


class BudgetManager:
    def __init__(self):
        self.data = load_data()

    def add_income(self, amount, source, note):
        item = {
            "type": "income",
            "amount": amount,
            "category": source,
            "description": note if note else source,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.data["transactions"].append(item)
        save_data(self.data)
        print("Income added successfully.")

    def add_expense(self, amount, category, note):
        item = {
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": note,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.data["transactions"].append(item)
        save_data(self.data)
        print("Expense added successfully.")

    def view_transactions(self):
        transactions = self.data["transactions"]
        print("\n--- All Transactions ---")

        if not transactions:
            print("No transactions found.")
            return

        for number, item in enumerate(transactions, 1):
            print(
                f"{number}. {item['date']} | "
                f"{item['type'].title():7} | "
                f"Rs. {item['amount']:.2f} | "
                f"{item['category']} | {item['description']}"
            )

    def show_summary(self):
        income, expense, balance = calculate_totals(self.data["transactions"])

        print("\n" + "=" * 45)
        print("               BUDGET SUMMARY")
        print("=" * 45)
        print(f"Total Income      : Rs. {income:.2f}")
        print(f"Total Expenses    : Rs. {expense:.2f}")
        print(f"Remaining Balance : Rs. {balance:.2f}")
        print("=" * 45)

        if balance < 0:
            print("Warning: Your expenses are higher than your income.")

    def show_categories(self):
        totals = category_totals(self.data["transactions"])

        print("\n--- Category-wise Expenses ---")
        if not totals:
            print("No expenses found.")
            return

        for category, amount in sorted(totals.items()):
            print(f"{category:<20} Rs. {amount:.2f}")

    def search_transactions(self, word):
        word = word.lower()
        found = []

        for item in self.data["transactions"]:
            text = (
                item["category"] + " " +
                item["description"] + " " +
                item["type"]
            ).lower()

            if word in text:
                found.append(item)

        print("\n--- Search Results ---")
        if not found:
            print("No matching transactions found.")
            return

        for number, item in enumerate(found, 1):
            print(
                f"{number}. {item['date']} | {item['type'].title()} | "
                f"Rs. {item['amount']:.2f} | "
                f"{item['category']} | {item['description']}"
            )

    def delete_transaction(self):
        transactions = self.data["transactions"]

        if not transactions:
            print("No transactions to delete.")
            return

        self.view_transactions()

        try:
            number = int(input("Enter transaction number to delete: "))
            if number < 1 or number > len(transactions):
                print("Invalid transaction number.")
                return

            removed = transactions.pop(number - 1)
            save_data(self.data)
            print(f"Deleted transaction: {removed['description']}")
        except ValueError:
            print("Please enter a valid number.")
