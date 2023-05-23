import slot_config
from deposit import deposit


def check_if_playing(*balance):
    answer = input("Would you like to play? (Y/n)").upper()

    if answer == "Y":
        return True
    else:
        if leaving_with_balance(balance):
            print("Thanks for playing!")
            quit()


def leaving_with_balance(balance):
    if len(balance) != 0:
        return True, print(f"Congrats! You left with ${balance[0]}")
    else:
        return True, print("You left with nothing. Better luck next time.")


def check_for_empty_balance(balance) -> int:
    if balance == 0:
        check_if_playing()
        balance = deposit()

    return balance


def input_is_digit(input):
    if input.isdigit():
        return True
    else:
        print("Please enter a number.")


def amount_is_greater_than_0(amount):
    if amount > 0:
        return True
    else:
        print("Amount must be greater than 0.")


def line_numbers_are_valid(lines):
    if 1 <= lines <= slot_config.MAX_LINES:
        return True
    else:
        print("Enter a valid number of lines.")


def player_bet_is_valid(player_bet):
    if slot_config.MIN_BET <= player_bet <= slot_config.MAX_BET:
        return True
    else:
        print(
            f"Amount must be between ${slot_config.MIN_BET} and ${slot_config.MAX_BET}.")


def check_to_add_balance():
    answer = input(
        "Would you like to add more to your balance to compete this bet? (Y/n)").upper()

    if answer == "Y":
        new_deposit = deposit()
        return new_deposit
    else:
        check_if_playing()


def enough_balance_for_bet(total_bet, balance):
    if total_bet > balance:
        print(
            f"You do not have enough to bet that amount, your current balance is: ${balance}")
    else:
        return True
