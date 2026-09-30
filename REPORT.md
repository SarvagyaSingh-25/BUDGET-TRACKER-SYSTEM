# Personal Budget Tracker - Project Report

## 1. Cover Page

**Project:** Personal Budget Tracker  
**Course:** Python Essentials  
**Type:** Command-Line Python Project

Student Name: ____________________  
Registration Number: ______________  
Section: __________________________  
Date: _____________________________

## 2. Introduction

Managing daily expenses is a common problem for students. Small expenses on food, travel, shopping, and other activities can become difficult to track.

This project provides a simple offline command-line application for recording income and expenses.

## 3. Problem Statement

Users need a simple way to record transactions and understand their remaining balance without using a complicated application.

## 4. Functional Requirements

The project supports:
- Adding income
- Adding expenses
- Viewing transactions
- Deleting transactions
- Searching transactions
- Calculating income and expenses
- Showing remaining balance
- Showing category-wise expenses
- Saving data locally

## 5. Non-functional Requirements

- Usability
- Reliability
- Maintainability
- Resource efficiency
- Basic error handling

## 6. System Architecture

The application follows a simple modular structure.

`main.py` handles the menu, `budget_manager.py` handles operations, `reports.py` performs calculations, `validators.py` validates input, and `storage.py` manages JSON storage.

See `docs/system_architecture.md`.

## 7. Design Diagrams

The repository contains:
- Use case diagram
- Workflow diagram
- Sequence diagram
- Class/component diagram
- Storage design

## 8. Design Decisions and Rationale

### JSON Storage
JSON was selected because it is simple and does not require a database server.

### Terminal Interface
A command-line interface keeps the project compatible with the course requirement for terminal execution.

### Modular Structure
The code is separated into files to make it easier to understand, test, and maintain.

## 9. Implementation Details

The application uses:
- Functions
- Classes
- Lists
- Dictionaries
- Loops
- Conditional statements
- File handling
- JSON
- Exception handling
- Basic unit testing

## 10. Results

The application can successfully add, display, search, and delete transactions and calculate budget information.

Suggested screenshots for the final report:
1. Main menu
2. Adding income
3. Adding expense
4. Transaction list
5. Budget summary
6. Category analysis
7. Test result

## 11. Testing Approach

Automated tests are provided in `tests/test_budget.py`.

Run:

```bash
python -m unittest discover
```

The tests check:
- Total calculation
- Category calculation
- Highest expense calculation

Manual testing should also cover invalid amounts, empty fields, invalid choices, and invalid transaction numbers.

## 12. Challenges Faced

Possible development challenges included:
- Handling invalid user input
- Keeping saved data after program exit
- Separating the program into modules
- Making calculations accurate

## 13. Learnings and Key Takeaways

This project helped demonstrate practical use of Python fundamentals, modular programming, file handling, JSON data, input validation, and basic testing.

## 14. Future Enhancements

- Monthly budget limits
- CSV export
- Date filters
- Recurring expenses
- Multiple user profiles
- Password protection

## 15. References

- Python documentation
- Course instructions provided through VITyarthi
- Python `json` module documentation
- Python `unittest` module documentation
