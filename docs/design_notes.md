# Design Notes

## Why JSON?

JSON was selected because the project is intended for beginners. It is easy to read, write, and inspect without setting up a database.

## Why Separate Files?

The program is divided into small files so each part has a clear responsibility.

## Why a Terminal Interface?

The course submission requires the project to be executable from a command line. A terminal menu also keeps the implementation focused on Python fundamentals.

## Main Data Format

Each transaction contains:

```text
type
amount
category
description
date
```

Example:

```json
{
    "type": "expense",
    "amount": 250,
    "category": "Food",
    "description": "Lunch",
    "date": "2026-09-30"
}
```
