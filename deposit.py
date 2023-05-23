import validate


def deposit() -> int:
    while True:
        amount = input("What would you like to deposit? $")

        if validate.input_is_digit(amount):
            amount = int(amount)
            if validate.amount_is_greater_than_0(amount):
                break

    return amount
