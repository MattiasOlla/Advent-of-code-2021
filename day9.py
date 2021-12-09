from functools import reduce
from operator import mul
from pathlib import Path
from pprint import pprint
from typing import Generator

filepath = Path(__file__)
data_path = filepath.parent / "data" / f"{filepath.stem}.txt"
data = [[int(x) for x in row] for row in data_path.read_text().splitlines()]


def neighbour_gen(
    data: list[list[int]], row: int, col: int
) -> Generator[tuple[int, int], None, None]:
    num_rows = len(data)
    num_cols = len(data[row])

    for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if 0 <= n_row < num_rows and 0 <= n_col < num_cols:
            yield n_row, n_col


def find_low_points(data: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i, row in enumerate(data)
        for j, height in enumerate(row)
        if all(height < data[r][c] for r, c in neighbour_gen(data, i, j))
    ]


def part1():
    low_point_heights = [data[i][j] for i, j in find_low_points(data)]
    risk_level = sum(low_point_heights) + len(low_point_heights)
    print(f"{risk_level=}")


def find_baisin_size(data: list[list[int]], row: int, col: int) -> int:
    baisin_coords = set()
    queue = [(row, col)]
    while queue:
        curr_row, curr_col = queue.pop(0)
        increasing_neighbours = [
            (neigh_row, neigh_col)
            for neigh_row, neigh_col in set(neighbour_gen(data, curr_row, curr_col)) - baisin_coords
            if (
                data[curr_row][curr_col] < data[neigh_row][neigh_col]
                and data[neigh_row][neigh_col] != 9
            )
        ]
        queue.extend(increasing_neighbours)
        baisin_coords.add((curr_row, curr_col))

    return len(baisin_coords)


def print_cutout(data: list[list[int]], row, col, window_size: int = 12) -> None:
    size = window_size // 2
    pprint(
        [
            data_row[max(col - size, 0) : min(col + size + 1, len(data_row))]
            for data_row in data[max(row - size, 0) : min(row + size + 1, len(data))]
        ]
    )


def part2():
    low_point_idx = find_low_points(data)
    baisin_sizes = [find_baisin_size(data, i, j) for i, j in low_point_idx]
    product = reduce(mul, sorted(baisin_sizes, reverse=True)[:3])
    print(f"{product=}")


if __name__ == "__main__":
    part1()
    part2()
