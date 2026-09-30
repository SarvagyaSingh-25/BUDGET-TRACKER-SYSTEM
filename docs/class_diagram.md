# Class / Component Diagram

```text
+-----------------------+
|     BudgetManager     |
+-----------------------+
| data                  |
+-----------------------+
| add_income()          |
| add_expense()         |
| view_transactions()   |
| show_summary()        |
| show_categories()     |
| search_transactions() |
| delete_transaction()  |
+-----------+-----------+
            |
            +------------------+
            |                  |
            v                  v
+------------------+   +------------------+
|     storage.py   |   |    reports.py    |
+------------------+   +------------------+
| load_data()      |   | calculate_totals |
| save_data()      |   | category_totals  |
+------------------+   | highest_expense  |
                       +------------------+
```
