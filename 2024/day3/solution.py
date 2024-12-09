import re


def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        text = input_file.read()

    return text


def read_mult_instructions(input_string: str) -> list[str]:
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return regex.findall(input_string)


def main():
    input_string = load_input("./2024/day3/input.txt")
    real_instructions = read_mult_instructions(input_string)
    return print("result: ", sum(int(x) * int(y) for x, y in real_instructions))


if __name__ == "__main__":
    main()
