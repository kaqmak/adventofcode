from typing import Literal


def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        row_list = [list(map(int, line.split())) for line in input_file.readlines()]

    return row_list


def diff(x_list: list[int]) -> list[int]:
    for i, x0 in enumerate(x_list[0:-1]):
        yield x_list[i + 1] - x0


def is_safe(x=list[int]) -> Literal[0, 1]:
    sign = 1 if x[1] - x[0] > 0 else -1
    return next((0 for d in diff(x) if not (sign * d > 0 and sign * d <= 3)), 1)


def is_safe_with_dampeners(x=list[int]) -> Literal[0, 1]:
    safe_at_first = is_safe(x)
    if safe_at_first == 1:
        return safe_at_first
    else:
        return any(is_safe(x[:i] + x[i + 1 :]) for i in range(len(x)))


def count_safe_reports(input_list: list[list[int]]) -> int:
    safe_reports = 0
    for row in input_list:
        safe_reports += is_safe_with_dampeners(row)
    return safe_reports


def main():
    input_list = load_input("./2024/day2/input.txt")
    safe_reports = count_safe_reports(input_list)
    print(safe_reports)


if __name__ == "__main__":
    main()
