def load_input(input_file_path: str) -> list[list[int]]:
    with open(input_file_path, "r") as input_file:
        row_list = [list(map(int, line.split())) for line in input_file.readlines()]

    columnar_list = list(zip(*row_list))
    return columnar_list


def sorted_columnar_list(columnar_list: list[list[int]]) -> tuple[list[int], list[int]]:
    x_sorted = sorted(columnar_list[0])
    y_sorted = sorted(columnar_list[1])
    return x_sorted, y_sorted


def total_distance(columnar_list: list[list[int]]) -> int:
    x_sorted, y_sorted = sorted_columnar_list(columnar_list)

    return sum(abs(x - y) for x, y in zip(x_sorted, y_sorted))


def similarity_score(sorted_columnar_list: tuple[list[int], list[int]]) -> int:
    x_sorted, y_sorted = sorted_columnar_list[0], sorted_columnar_list[1]
    count = [0] * len(x_sorted)
    similarity = [0] * len(x_sorted)
    start_idx_y = 0
    for i_x, x in enumerate(x_sorted):
        for i_y, y in enumerate(y_sorted[start_idx_y:], start=start_idx_y):
            if y < x:
                continue
            if y == x:
                count[i_x] += 1
            if y > x:
                similarity[i_x] = count[i_x] * x
                start_idx_y = i_y
                break
    return sum(similarity)


def main():
    input_list = load_input("./2024/day1/input.txt")
    columnar_list = sorted_columnar_list(input_list)
    print("total distance:", total_distance(columnar_list))
    print("similarity score:", similarity_score(sorted_columnar_list(input_list)))


if __name__ == "__main__":
    main()
