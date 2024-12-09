import re
from collections import deque


def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        text = input_file.read()

    return text


def read_enabled_instructions(
    input_string: str, enabler_string="do()", disabler_string="don't()"
) -> list[str]:
    len_dont = len(disabler_string)
    len_do = len(enabler_string)
    stack = deque(maxlen=len_dont)

    enabled = True
    enabled_string = ""
    for char in input_string:
        stack.append(char)
        if "".join(stack) == disabler_string:
            enabled = False
        elif "".join(stack)[-1 * len_do - 1 : -1] == enabler_string:
            enabled = True

        if enabled:
            enabled_string += char

    return enabled_string


def read_mult_instructions(input_string: str) -> list[str]:
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return regex.findall(input_string)


def main():
    input_string = load_input("./2024/day3/input.txt")
    enabled_string = read_enabled_instructions(input_string)
    print(
        "solution:",
        sum(int(x) * int(y) for x, y in read_mult_instructions(enabled_string)),
    )


if __name__ == "__main__":
    main()
