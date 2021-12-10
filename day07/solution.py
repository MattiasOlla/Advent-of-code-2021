from pathlib import Path
from typing import Callable, Generator

data_path = Path(__file__) / "data.txt"
data = [int(x) for x in data_path.read_text().split(",")]


def distance_gen(
    level: int, func: Callable[[int], int] = lambda x: x
) -> Generator[int, None, None]:
    for x in data:
        yield func(abs(x - level))


def part1():
    print(min((sum(distance_gen(level)), level) for level in range(min(data), max(data) + 1)))


def part2():
    print(
        min(
            (sum(distance_gen(level, lambda x: x * (x + 1) // 2)), level)
            for level in range(min(data), max(data) + 1)
        )
    )


if __name__ == "__main__":
    part1()
    part2()
