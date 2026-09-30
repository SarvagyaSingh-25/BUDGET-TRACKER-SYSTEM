import unittest
from reports import calculate_totals, category_totals, highest_expense


class TestReports(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {
                "type": "income",
                "amount": 10000,
                "category": "Pocket Money",
                "description": "Monthly money"
            },
            {
                "type": "expense",
                "amount": 500,
                "category": "Food",
                "description": "Lunch"
            },
            {
                "type": "expense",
                "amount": 1000,
                "category": "Travel",
                "description": "Bus and auto"
            },
            {
                "type": "expense",
                "amount": 300,
                "category": "Food",
                "description": "Snacks"
            }
        ]

    def test_totals(self):
        income, expense, balance = calculate_totals(self.transactions)
        self.assertEqual(income, 10000)
        self.assertEqual(expense, 1800)
        self.assertEqual(balance, 8200)

    def test_categories(self):
        result = category_totals(self.transactions)
        self.assertEqual(result["Food"], 800)
        self.assertEqual(result["Travel"], 1000)

    def test_highest_expense(self):
        result = highest_expense(self.transactions)
        self.assertEqual(result["amount"], 1000)


if __name__ == "__main__":
    unittest.main()
