import validate


def get_bet():
    while True:
        player_bet = input("What would you like to bet on each line? $")
        if validate.input_is_digit(player_bet):
            player_bet = int(player_bet)
            if validate.player_bet_is_valid(player_bet):
                break

    return player_bet
