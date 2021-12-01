from pathlib import Path
from typing import Generator, TypeVar

T = TypeVar("T")


def iter_tuples(lst: list[T], num: int) -> Generator[tuple[T, ...], None, None]:
    for start_idx in range(len(lst) - num + 1):
        yield tuple(lst[start_idx : start_idx + num])


data_path = Path(__file__).parent / "data" / "day1.txt"
numbers = [int(line) for line in data_path.read_text().splitlines()]

num_increasing = sum(val0 < val1 for val0, val1 in iter_tuples(numbers, 2))
print(f"Number of increasing pairs: {num_increasing}")

sliding_sum = [sum(window) for window in iter_tuples(numbers, 3)]
num_increasing_sliding_sum = sum(
    val0 < val1 for val0, val1 in iter_tuples(sliding_sum, 2)
)
print(f"Number of increasing smoothed: {num_increasing_sliding_sum}")
