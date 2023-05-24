from get_slot_machine_spin import get_slot_machine_spin
from print_slot_machine import print_slot_machine
from get_number_of_lines import get_number_of_lines
from get_bet import get_bet
from check_winnings import check_winnings
import slot_config
import validate
import time


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if validate.enough_balance_for_bet(total_bet, balance):
            break
        else:
            new_deposit = validate.check_to_add_balance()
            print(f"You deposited ${new_deposit}")
            return new_deposit

    print(
        f"You are betting ${bet} on {lines} line(s). Total bet is equal to: ${total_bet}")
    time.sleep(1)
    print(
        f"All bets locked in. You bet ${total_bet}. Your remaining balance: ${balance - total_bet}")
    time.sleep(2)

    slots = get_slot_machine_spin(
        slot_config.ROWS, slot_config.COLS, slot_config.symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(
        slots, lines, bet, slot_config.symbol_value)

    if winnings:
        print(f"You won ${winnings}.")
    else:
        print("Better luck next time.")
    if winning_lines:
        print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet
