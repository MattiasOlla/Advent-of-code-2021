from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

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
    0: frozenset("abcefg"),
    1: frozenset("cf"),
    2: frozenset("acdeg"),
    3: frozenset("acdfg"),
    4: frozenset("bcdf"),
    5: frozenset("abdfg"),
    6: frozenset("abdefg"),
    7: frozenset("acf"),
    8: frozenset("abcdefg"),
    9: frozenset("abcdfg"),
}
segment_counts = {digit: len(segments) for digit, segments in digits.items()}


def pop_where_num_overlap(
    segment_list: list[frozenset[str]], to_match: frozenset[str], num_overlap: int
) -> frozenset[str]:
    matched = next(digit for digit in segment_list if len(digit & to_match) == num_overlap)
    segment_list.remove(matched)
    return matched


@dataclass
class Line:
    signal_patterns: list[frozenset[str]]
    output_values: list[frozenset[str]]

    @classmethod
    def from_str(cls, text: str) -> "Line":
        signal_str, _, output_str = text.partition(" | ")
        signal_patterns = [frozenset(digit) for digit in signal_str.split()]
        output_values = [frozenset(digit) for digit in output_str.split()]
        return cls(signal_patterns=signal_patterns, output_values=output_values)

    def decode(self) -> dict[frozenset[str], int]:
        # Group by segment count
        length_groups: defaultdict[int, list[frozenset[str]]] = defaultdict(list)
        for segment in self.signal_patterns:
            length_groups[len(segment)].append(segment)

        one = length_groups[2].pop()
        seven = length_groups[3].pop()
        four = length_groups[4].pop()
        eight = length_groups[7].pop()

        # 1 is c and f segments
        cf_segments = one

        # b and d elements differ between 4 and 1
        bd_segments = four - one

        # Of length six segments, only 6 has only one of c and f
        six = pop_where_num_overlap(length_groups[6], to_match=cf_segments, num_overlap=1)

        # Of length six segments, only 9 has both b and d
        nine = pop_where_num_overlap(length_groups[6], to_match=bd_segments, num_overlap=2)

        # Of length six elements, only 0 remains
        zero = length_groups[6].pop()

        # Of length five elements, only 3 has both c and f
        three = pop_where_num_overlap(length_groups[5], to_match=cf_segments, num_overlap=2)

        # Of length five elements, only 5 has both b and d
        five = pop_where_num_overlap(length_groups[5], to_match=bd_segments, num_overlap=2)

        # Of length five elements, only 2 remains
        two = length_groups[5].pop()

        return {
            one: 1,
            seven: 7,
            four: 4,
            eight: 8,
            six: 6,
            nine: 9,
            zero: 0,
            three: 3,
            five: 5,
            two: 2,
        }

    def get_decoded_output(self) -> int:
        decode_map = self.decode()
        return sum(
            decode_map[output] * 10 ** i for i, output in enumerate(reversed(self.output_values))
        )


data = [Line.from_str(s) for s in data_path.read_text().splitlines()]


def part1():
    lengths = {segment_counts[i] for i in [1, 4, 7, 8]}
    counts = sum(len(x) in lengths for line in data for x in line.output_values)
    print(counts)


def part2():
    output_sum = sum(line.get_decoded_output() for line in data)
    print(output_sum)


if __name__ == "__main__":
    part1()
    part2()
