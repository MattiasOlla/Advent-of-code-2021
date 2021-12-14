from collections import Counter
from itertools import chain, zip_longest
from pathlib import Path
from typing import TypeAlias

DataType: TypeAlias = tuple[str, dict[str, str]]

data_path = Path(__file__).parent / "data.txt"


def parse_data(text: str) -> DataType:
    template, _, rules_str = text.partition("\n\n")
    rules = {k: v for line in rules_str.splitlines() for k, _, v in [line.partition(" -> ")]}
    return template, rules


def increment_polymer(polymer: str, rules: dict[str, str]) -> str:
    new_parts = [rules[x1 + x2] for x1, x2 in zip(polymer[:-1], polymer[1:])]
    return "".join(chain.from_iterable(zip_longest(polymer, new_parts, fillvalue="")))


def counts_recursive(polymer: str, rules: dict[str, str], depth: int) -> Counter:
    if depth == 0:
        return Counter(polymer)

    polymer = increment_polymer(polymer, rules)

    chunk_size = 10 ** 7
    counts = Counter()

    for i in range(0, len(polymer), chunk_size):
        print(f"Level {depth - 1} Processing {i} through {min(i + chunk_size, len(polymer))}")
        counts += counts_recursive(polymer[i : i + chunk_size + 1], rules, depth - 1)
        if i > 0:
            counts[polymer[i]] -= 1

    return counts


def part1(data: DataType) -> int:
    polymer, rules = data
    counts = counts_recursive(polymer, rules, depth=10)

    (_, most_common), *_, (_, least_common) = counts.most_common()
    return most_common - least_common


def part2(data: DataType) -> int:
    polymer, rules = data
    counts = counts_recursive(polymer, rules, depth=40)
    (_, most_common), *_, (_, least_common) = counts.most_common()
    return most_common - least_common


if __name__ == "__main__":
    data = parse_data(data_path.read_text())
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result: {part2(data)}")
