from spin import spin
import validate


def main():
    balance = 0
    print("Welcome to the Python Slot Machine!")
    while True:
        balance = int(validate.check_for_empty_balance(balance))
        print(f"Your balance is ${balance}")
        if validate.check_if_playing(balance):
            balance += spin(balance)


main()
