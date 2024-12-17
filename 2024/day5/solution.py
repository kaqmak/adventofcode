from pathlib import Path


def load_input(input_file_path: Path) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        text = input_file.read()

    return text


def split_orders_and_numbers(
    text: str,
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    text_split = text.split("\n\n", maxsplit=2)

    page_orders = [
        tuple(map(int, page_order_string.split("|", maxsplit=2)))
        for page_order_string in text_split[0].splitlines()
    ]
    updates = [list(map(int, line.split(","))) for line in text_split[1].splitlines()]
    return page_orders, updates


def page_orders_to_dict(page_orders: list[tuple[int, int]]) -> dict[str, list[int]]:
    page_orders_dict = {}
    for page_order in page_orders:
        page_1 = page_order[0]
        page_2 = page_order[1]
        if page_1 not in page_orders_dict:
            page_orders_dict[page_1] = []
        page_orders_dict[page_1].append(page_2)
    return page_orders_dict


def is_correct_order(
    page_orders_dict: dict[str, list[int]], updates: list[int]
) -> bool:
    for i, page_1 in enumerate(updates):
        for j, page_2 in enumerate(updates[i + 1 :], start=i + 1):
            if page_orders_dict.get(page_2) and page_1 in page_orders_dict.get(page_2):
                return False
            else:
                continue

    return True


def middle_element(lst: list[int]) -> int:
    return lst[len(lst) // 2]


def correctly_ordered_middle_elements(
    page_orders_dict: dict[str, list[int]], all_updates: list[list[int]]
) -> list[int]:
    middle_elements = []
    for updates in all_updates:
        if is_correct_order(page_orders_dict, updates):
            middle_elements.append(middle_element(updates))
    return middle_elements


def main():
    input_file_path = Path("./2024/day5/input.txt")
    text = load_input(input_file_path)
    page_orders, updates = split_orders_and_numbers(text)
    page_orders_dict = page_orders_to_dict(page_orders)
    print(sum(correctly_ordered_middle_elements(page_orders_dict, updates)))


if __name__ == "__main__":
    main()
