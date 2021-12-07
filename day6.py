from collections import Counter
from pathlib import Path
from typing import Generator

filepath = Path(__file__)
data_path = filepath.parent / "data" / f"{filepath.stem}.txt"
counts = Counter(int(x) for x in data_path.read_text().split(","))


def tick_single(num: int) -> Generator[int, None, None]:
    if num == 0:
        yield 6
        yield 8
    else:
        yield num - 1


def tick_multiple(nums: list[int]) -> list[int]:
    return [new for num in nums for new in tick_single(num)]


def tick_counts(counts: Counter[int]) -> Counter[int]:
    new_counts = Counter()
    for num, count in counts.items():
        if num == 0:
            new_counts[6] += count
            new_counts[8] += count
        else:
            new_counts[num - 1] += count
    return new_counts


def iterate(num_days: int) -> int:
    x = counts
    for _ in range(num_days):
        x = tick_counts(x)
    return sum(x.values())


def part1():
    total = iterate(80)
    print(f"After 80 iterations: {total}")


def part2():
    total = iterate(256)
    print(f"After 256 iterations: {total}")


if __name__ == "__main__":
    part1()
    part2()
