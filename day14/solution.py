from collections import Counter
from pathlib import Path
from typing import TypeAlias

DataType: TypeAlias = tuple[str, dict[str, str]]

data_path = Path(__file__).parent / "data.txt"


def parse_data(text: str) -> DataType:
    template, _, rules_str = text.partition("\n\n")
    rules = {k: v for line in rules_str.splitlines() for k, _, v in [line.partition(" -> ")]}
    return template, rules


def count_pairs(polymer: str, rules: dict[str, str], num_iter: int):
    pair_map = {(k[0], k[1]): [(k[0], v), (v, k[1])] for k, v in rules.items()}

    pairs = Counter(zip(" " + polymer, polymer + " "))
    for _ in range(num_iter):
        counts = Counter()
        for pair, num in pairs.items():
            for new_pair in pair_map.get(pair, [pair]):
                counts[new_pair] += num
        pairs = counts
    return pairs


def pair_counts_to_final(pair_counts: Counter[tuple[str, str]]) -> Counter[str]:
    double_counts: Counter[str] = Counter()
    for pair, count in pair_counts.items():
        for letter in pair:
            if letter != " ":
                double_counts[letter] += count
    return Counter({p: c // 2 for p, c in double_counts.items()})


def solution(polymer: str, rules: dict[str, str], num_iter: int) -> int:
    pair_counts = count_pairs(polymer, rules, num_iter)
    counts = pair_counts_to_final(pair_counts)

    (_, most_common), *_, (_, least_common) = counts.most_common()
    return most_common - least_common


def part1(data: DataType) -> int:
    return solution(*data, 10)


def part2(data: DataType) -> int:
    return solution(*data, 40)


if __name__ == "__main__":
    data = parse_data(data_path.read_text())
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result: {part2(data)}")
