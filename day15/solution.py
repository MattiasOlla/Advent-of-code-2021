from __future__ import annotations

from collections import deque
from functools import cache
from pathlib import Path
from typing import Generator, TypeAlias

DataType: TypeAlias = list[list[int]]

data_path = Path(__file__).parent / "data.txt"


def parse_data(text: str) -> DataType:
    return [[int(x) for x in line] for line in text.splitlines()]


@cache
def neighbours_gen(row: int, col: int, grid_size: int) -> Generator[tuple[int, int], None, None]:
    if row > 0:
        yield row - 1, col
    if row < grid_size - 1:
        yield row + 1, col
    if col > 0:
        yield row, col - 1
    if col < grid_size - 1:
        yield row, col + 1


def find_safest_path_risk(grid: list[list[int]]) -> int:
    size = len(grid)
    stack: deque[tuple[int, int]] = deque([(0, 0)])

    lowest_risks = [
        [0 if (row, col) == (0, 0) else None for col in range(size)] for row in range(size)
    ]

    while stack:
        row, col = stack.popleft()
        lowest = lowest_risks[row][col]
        assert lowest is not None

        for neigh_row, neigh_col in neighbours_gen(row, col, size):
            neigh_risk = lowest + grid[neigh_row][neigh_col]
            neigh_lowest = lowest_risks[neigh_row][neigh_col]

            if neigh_lowest is None or neigh_risk < neigh_lowest:
                lowest_risks[neigh_row][neigh_col] = neigh_risk
                stack.append((neigh_row, neigh_col))

    target_lowest = lowest_risks[-1][-1]
    assert target_lowest
    return target_lowest


def part1(data: DataType) -> int:
    return find_safest_path_risk(data)


def extend_data(grid: list[list[int]], num_repeat: int = 5) -> list[list[int]]:
    size = len(grid)

    def new_val(row: int, col: int) -> int:
        row_repeat_num = row // size
        col_repeat_num = col // size

        original = grid[row % size][col % size]
        increased = original + row_repeat_num + col_repeat_num
        return (increased - 1) % 9 + 1

    return [
        [new_val(row, col) for col in range(num_repeat * size)] for row in range(num_repeat * size)
    ]


def part2(data: DataType) -> int:
    extended_grid = extend_data(data)
    return find_safest_path_risk(extended_grid)


if __name__ == "__main__":
    data = parse_data(data_path.read_text())
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result: {part2(data)}")
