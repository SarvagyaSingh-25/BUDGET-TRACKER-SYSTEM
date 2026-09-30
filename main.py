from budget_manager import BudgetManager
from validators import get_amount, get_text


def show_menu():
    print("\n" + "=" * 45)
    print("           PERSONAL BUDGET TRACKER")
    print("=" * 45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Budget Summary")
    print("5. Category-wise Expenses")
    print("6. Search Transactions")
    print("7. Delete Transaction")
    print("8. Exit")
    print("=" * 45)


def add_income(manager):
    print("\n--- Add Income ---")
    amount = get_amount()
    source = get_text("Enter income source: ")
    note = input("Enter note (optional): ").strip()
    manager.add_income(amount, source, note)


def add_expense(manager):
    print("\n--- Add Expense ---")
    amount = get_amount()
    category = get_text("Enter expense category: ")
    note = get_text("Enter description: ")
    manager.add_expense(amount, category, note)


def main():
    manager = BudgetManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_income(manager)
        elif choice == "2":
            add_expense(manager)
        elif choice == "3":
            manager.view_transactions()
        elif choice == "4":
            manager.show_summary()
        elif choice == "5":
            manager.show_categories()
        elif choice == "6":
            word = get_text("Enter word to search: ")
            manager.search_transactions(word)
        elif choice == "7":
            manager.delete_transaction()
        elif choice == "8":
            print("\nThank you for using Personal Budget Tracker.")
            break
        else:
            print("Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
