# Personal Budget Tracker

## 1. Project Overview

Personal Budget Tracker is a beginner-friendly command-line Python application.

The project helps a user record daily income and expenses and understand their remaining balance. It also provides a simple category-wise view of expenses and a search option.

The application does not use a graphical interface. Everything is performed through the terminal.

## 2. Main Features

- Add income
- Add expenses
- View all transactions
- Delete transactions
- Search transactions
- Calculate total income
- Calculate total expenses
- Calculate remaining balance
- Show category-wise expenses
- Store data locally in JSON
- Validate user input
- Run basic automated tests

## 3. Technologies Used

- Python 3
- JSON
- `datetime`
- `unittest`
- Git/GitHub

No third-party Python packages are required.

## 4. Requirements

Install Python 3.8 or newer.

Check Python:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

## 5. Project Structure

```text
personal-budget-tracker/
│
├── main.py
├── budget_manager.py
├── storage.py
├── validators.py
├── reports.py
├── expense_manager.py
├── income_manager.py
│
├── data/
│   └── budget_data.json
│
├── tests/
│   └── test_budget.py
│
├── README.md
├── statement.md
```

## 6. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd personal-budget-tracker
```

There are no external dependencies.

If desired, create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

## 7. Run the Project

Run:

```bash
python main.py
```

The program displays a menu:

```text
1. Add Income
2. Add Expense
3. View Transactions
4. Budget Summary
5. Category-wise Expenses
6. Search Transactions
7. Delete Transaction
8. Exit
```

## 8. Data Storage

Transaction information is stored in:

```text
data/budget_data.json
```

The program creates the file automatically if it does not exist.

## 9. Testing

Run all tests:

```bash
python -m unittest discover
```

Expected result:

```text
Ran 3 tests

OK
```

## 10. Example

```text
--- Add Income ---
Enter amount: 20000
Enter income source: Pocket Money
Enter note (optional): September money
Income added successfully.

--- Add Expense ---
Enter amount: 350
Enter expense category: Food
Enter description: Lunch
Expense added successfully.
```

The summary will then show the calculated income, expense, and balance.

## 11. Error Handling

The project handles:

- Non-numeric amounts
- Zero or negative amounts
- Empty text fields
- Invalid menu choices
- Invalid transaction numbers
- Missing data files
- Invalid JSON data

## 12. Future Improvements

Possible future versions could include:

- Monthly budget limits
- CSV export
- Monthly reports
- Date filters
- Password protection
- Recurring expenses
- Saving separate budgets for different users
