import validate
import slot_config


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(slot_config.MAX_LINES) + ")? ")

        if validate.input_is_digit(lines):
            lines = int(lines)
            if validate.line_numbers_are_valid(lines):
                break

    return lines
