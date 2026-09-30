# System Architecture

```text
              +----------------+
              |     User       |
              +-------+--------+
                      |
                      v
              +----------------+
              |    main.py     |
              |  Menu / Input  |
              +-------+--------+
                      |
                      v
              +----------------+
              | BudgetManager  |
              +---+--------+---+
                  |        |
          +-------+        +--------+
          v                          v
+------------------+        +------------------+
|    validators    |        |     reports      |
+------------------+        +--------+---------+
                                      |
                                      v
                              +---------------+
                              |    storage    |
                              +-------+-------+
                                      |
                                      v
                              +---------------+
                              | budget_data   |
                              |    .json      |
                              +---------------+
```

## Explanation

The user interacts with the application through the terminal.

`main.py` displays the menu and takes user choices.

`BudgetManager` performs the main budget operations.

`validators.py` checks user input.

`reports.py` calculates totals and category information.

`storage.py` reads and writes the JSON data file.

The JSON file provides persistent local storage.
