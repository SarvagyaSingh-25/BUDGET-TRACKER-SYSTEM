def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def get_text(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")
