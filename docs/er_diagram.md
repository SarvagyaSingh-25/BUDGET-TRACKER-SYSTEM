# Storage Design

The project uses a JSON file instead of a relational database.

```text
BUDGET_DATA
    |
    +--- transactions
             |
             +--- type
             +--- amount
             +--- category
             +--- description
             +--- date
```

Each transaction is one record in the `transactions` list.
