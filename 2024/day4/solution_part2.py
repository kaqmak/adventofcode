import enum
from typing import Iterator


def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        row_list = [list(line) for line in input_file.readlines()]

    return row_list


class XDirection(enum.Enum):
    MINUS45 = 1
    PLUS45 = 2


def x_tracer(
    row_idx: int, col_idx: int, num_rows: int, num_cols: int, mode: XDirection
) -> Iterator[tuple[int, int]]:
    match mode:
        case XDirection.MINUS45:
            adder = (1, 1)
        case XDirection.PLUS45:
            adder = (-1, 1)

    off_set_row_idx = row_idx - adder[0]
    off_set_col_idx = col_idx - adder[1]
    while (
        off_set_row_idx < num_rows
        and off_set_col_idx < num_cols
        and off_set_row_idx >= 0
        and off_set_col_idx >= 0
    ):
        yield (off_set_row_idx, off_set_col_idx)
        row_idx = row_idx + adder[0]
        col_idx = col_idx + adder[1]
        off_set_row_idx = row_idx - adder[0]
        off_set_col_idx = col_idx - adder[1]


def find_key_words(
    row_idx: int, col_idx: int, letters: list[list[int]], key_word: str = "MAS"
) -> int:
    num_words = 0
    for direction in XDirection:
        word = ""
        for i, (r, c) in enumerate(
            x_tracer(row_idx, col_idx, len(letters), len(letters[0]), direction)
        ):
            if i >= len(key_word):
                break
            if key_word[i] != letters[r][c] and key_word[-1 - i] != letters[r][c]:
                break
            word += letters[r][c]

        if word == key_word or word[::-1] == key_word:
            num_words += 1
    return num_words // 2


def find_all_keys_words(letters: list[list[int]], key_word: str = "MAS") -> int:
    num_words = 0
    for row_idx in range(len(letters)):
        for col_idx in range(len(letters[0])):
            num_words += find_key_words(row_idx, col_idx, letters, key_word)
    return num_words


def main():
    input_file_path = "./2024/day4/input.txt"
    letters = load_input(input_file_path)
    # letters = [
    #     list("MMMSXXMASM"),
    #     list("MSAMXMSMSA"),
    #     list("AMXSXMAAMM"),
    #     list("MSAMASMSMX"),
    #     list("XMASAMXAMM"),
    #     list("XXAMMXXAMA"),
    #     list("SMSMSASXSS"),
    #     list("SAXAMASAAA"),
    #     list("MAMMMXMMMM"),
    #     list("MXMXAXMASX"),
    # ]

    key_word = "MAS"

    print(find_all_keys_words(letters, key_word))
    # print(
    #     list(
    #         x_tracer(
    #             row_idx=3,
    #             col_idx=3,
    #             num_rows=len(letters),
    #             num_cols=len(letters[0]),
    #             mode=XDirection.MINUS45,
    #         )
    #     )
    # )


if __name__ == "__main__":
    main()
