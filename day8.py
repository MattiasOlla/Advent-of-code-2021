from dataclasses import dataclass
from pathlib import Path
from typing import Counter

filepath = Path(__file__)
data_path = filepath.parent / "data" / f"{filepath.stem}.txt"


#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
segment_counts = {digit: len(segments) for digit, segments in digits.items()}


@dataclass
class Line:
    signal_patterns: list[str]
    output_values: list[str]

    @classmethod
    def from_str(cls, text: str) -> "Line":
        signal_str, _, output_str = text.partition(" | ")
        return cls(signal_patterns=signal_str.split(), output_values=output_str.split())


data = [Line.from_str(s) for s in data_path.read_text().splitlines()]


def part1():
    lengths = {segment_counts[i] for i in [1, 4, 7, 8]}
    counts = sum(len(x) in lengths for line in data for x in line.output_values)
    print(counts)


if __name__ == "__main__":
    part1()
