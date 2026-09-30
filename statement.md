# Project Statement

## Project Title

Personal Budget Tracker

## Problem Statement

Students often make several small transactions during a month. Without keeping a record, it can become difficult to understand how much money was received, how much was spent, and where the money was spent.

The Personal Budget Tracker provides a simple command-line solution for recording income and expenses and calculating the current balance.

## Scope

The project covers basic personal budget management using a local JSON file.

The application can:
- Record income
- Record expenses
- Display transactions
- Delete transactions
- Search transactions
- Calculate totals
- Group expenses by category

The application does not connect to banks, process payments, or provide financial advice.

## Target Users

- Students
- Beginners learning Python
- Users who want a simple offline expense tracker

## Functional Requirements

### FR1 - Add Income
The user can enter an amount, source, and optional note.

### FR2 - Add Expense
The user can enter an amount, category, and description.

### FR3 - View Transactions
The user can see stored transactions with date, type, amount, category, and description.

### FR4 - Delete Transaction
The user can select a transaction number and remove it.

### FR5 - Budget Summary
The program calculates total income, total expenses, and remaining balance.

### FR6 - Category Analysis
The program calculates total spending for each expense category.

### FR7 - Search
The user can search transactions using a word such as Food, Travel, or income.

### FR8 - Data Storage
Transactions are saved in a JSON file.

## Non-functional Requirements

### Usability
The menu uses simple words and numbered choices.

### Reliability
The application validates important user inputs and handles invalid data without closing unexpectedly.

### Maintainability
Different responsibilities are placed in separate Python files.

### Resource Efficiency
The application uses a small local JSON file and does not require an internet connection or database server.

## Software Modules

1. Main menu module
2. Budget management module
3. Storage module
4. Validation module
5. Reports and analysis module
6. Income helper module
7. Expense helper module

## Tools

- Python
- JSON
- Git
- GitHub

## Future Scope

The project can later support monthly limits, CSV reports, date filtering, recurring transactions, and multiple user profiles.
