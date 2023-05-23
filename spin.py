from get_slot_machine_spin import get_slot_machine_spin
from print_slot_machine import print_slot_machine
from get_number_of_lines import get_number_of_lines
from get_bet import get_bet
from check_winnings import check_winnings
import slot_config
import validate


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if validate.enough_balance_for_bet(total_bet, balance):
            break
        else:
            balance += validate.check_to_add_balance()

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(
        slot_config.ROWS, slot_config.COLS, slot_config.symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(
        slots, lines, bet, slot_config.symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet
