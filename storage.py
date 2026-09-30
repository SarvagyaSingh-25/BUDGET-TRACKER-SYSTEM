import json
import os


FILE_NAME = os.path.join("data", "budget_data.json")


def load_data():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):
        data = {"transactions": []}
        save_data(data)
        return data

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if "transactions" not in data:
            data["transactions"] = []

        return data

    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with empty data.")
        data = {"transactions": []}
        save_data(data)
        return data


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
