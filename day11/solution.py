import itertools
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generator, TypeAlias

DataType: TypeAlias = list[list["Octopus"]]

data_path = Path(__file__).parent / "data.txt"


@dataclass
class Octopus:
    energy_level: int
    has_flashed: bool = True

    def increase(self) -> bool:
        if self.has_flashed:
            return False
        if self.energy_level == 9:
            self.energy_level = 0
            self.has_flashed = True
            return True
        self.energy_level += 1
        return False

    def reset(self):
        self.has_flashed = False


class Grid:
    def __init__(self, text: str) -> None:
        self.grid = parse_data(text)
        self.size = len(self.grid)

    def energy_levels(self) -> list[list[int]]:
        return [[octo.energy_level for octo in row] for row in self.grid]

    def __str__(self) -> str:
        return "\n".join("".join(str(octo.energy_level) for octo in row) for row in self.grid)

    def increase_all_levels(self) -> list[tuple[int, int]]:
        flashes = [
            (i, j)
            for i, row in enumerate(self.grid)
            for j, octopus in enumerate(row)
            if octopus.increase()
        ]
        return flashes

    def neigbours(self, row: int, col: int) -> Generator[tuple[int, int], None, None]:
        for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]):
            neigh_row, neigh_col = row + i, col + j
            if (
                (neigh_row, neigh_col) != (row, col)
                and 0 <= neigh_row < self.size
                and 0 <= neigh_col < self.size
            ):
                yield (neigh_row, neigh_col)

    def step(self) -> int:
        for row in self.grid:
            for octo in row:
                octo.reset()

        flashes = self.increase_all_levels()
        num_flashes = len(flashes)
        while flashes:
            flash = flashes.pop(0)
            for neigbour_row, neigbour_col in self.neigbours(*flash):
                if self.grid[neigbour_row][neigbour_col].increase():
                    flashes.append((neigbour_row, neigbour_col))
                    num_flashes += 1
        return num_flashes


def parse_data(text: str) -> DataType:
    return [[Octopus(int(x)) for x in line] for line in text.strip().splitlines()]


def part1(text: str) -> int:
    grid = Grid(text)
    return sum(grid.step() for _ in range(100))


def part2(text: str) -> int:
    grid = Grid(text)
    for step in range(1, 10000 + 1):
        num_flashes = grid.step()
        if num_flashes == grid.size ** 2:
            return step
    return -1


if __name__ == "__main__":
    data = data_path.read_text()
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result: {part2(data)}")
