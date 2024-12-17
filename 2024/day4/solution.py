import enum
from typing import Iterator


def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        row_list = [list(line) for line in input_file.readlines()]

    return row_list


class Direction(enum.Enum):
    DOWN_RIGHT = 1
    UP_RIGHT = 2
    DOWN_LEFT = 3
    UP_LEFT = 4
    LEFT = 5
    RIGHT = 6
    UP = 7
    DOWN = 8


def tracer(
    row_idx: int, col_idx: int, num_rows: int, num_cols: int, mode: Direction
) -> Iterator[tuple[int, int]]:
    match mode:
        case Direction.DOWN_RIGHT:
            adder = (1, 1)
        case Direction.UP_RIGHT:
            adder = (-1, 1)
        case Direction.DOWN_LEFT:
            adder = (1, -1)
        case Direction.UP_LEFT:
            adder = (-1, -1)
        case Direction.LEFT:
            adder = (0, -1)
        case Direction.RIGHT:
            adder = (0, 1)
        case Direction.UP:
            adder = (-1, 0)
        case Direction.DOWN:
            adder = (1, 0)

    while row_idx < num_rows and col_idx < num_cols and row_idx >= 0 and col_idx >= 0:
        yield (row_idx, col_idx)
        row_idx = row_idx + adder[0]
        col_idx = col_idx + adder[1]


def find_key_words(
    row_idx: int, col_idx: int, letters: list[list[int]], key_word: str = "XMAS"
) -> list[list[int]]:
    num_words = 0
    for direction in Direction:
        word = ""
        for i, (r, c) in enumerate(
            tracer(row_idx, col_idx, len(letters), len(letters[0]), direction)
        ):
            if i >= len(key_word):
                break
            if key_word[i] != letters[r][c]:
                break
            word += letters[r][c]

        if word == key_word:
            num_words += 1
    return num_words


def find_all_keys_words(letters: list[list[int]], key_word: str = "XMAS") -> int:
    num_words = 0
    for row_idx in range(len(letters)):
        for col_idx in range(len(letters[0])):
            num_words += find_key_words(row_idx, col_idx, letters, key_word)
    return num_words


def main():
    input_file_path = "./2024/day4/input.txt"
    letters = load_input(input_file_path)

    key_word = "XMAS"

    print(find_all_keys_words(letters, key_word))


if __name__ == "__main__":
    main()
