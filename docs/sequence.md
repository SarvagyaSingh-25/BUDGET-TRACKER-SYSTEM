# Sequence Diagram - Add Expense

```text
User        main.py       BudgetManager       storage.py
 |             |                |                |
 |--expense--->|                |                |
 |             |--amount------->|                |
 |             |--category----->|                |
 |             |--description-->|                |
 |             |                |--save_data---->|
 |             |                |<---saved--------|
 |             |<--success------|                |
 |<--message---|                |                |
```
