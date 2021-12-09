from pathlib import Path
from tkinter.messagebox import NO
from typing import Generator

filepath = Path(__file__)
data_path = filepath.parent / "data" / f"{filepath.stem}.txt"
data = [[int(x) for x in row] for row in data_path.read_text().splitlines()]


def neighbour_gen(data: list[list[int]], row: int, col: int) -> Generator[int, None, None]:
    num_rows = len(data)
    num_cols = len(data[row])

    for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if 0 <= n_row < num_rows and 0 <= n_col < num_cols:
            yield data[n_row][n_col]


def part1():
    low_point_heights = [
        height
        for i, row in enumerate(data)
        for j, height in enumerate(row)
        if all(height < neighbour for neighbour in neighbour_gen(data, i, j))
    ]
    risk_level = sum(low_point_heights) + len(low_point_heights)
    print(f"{risk_level=}")


if __name__ == "__main__":
    part1()
