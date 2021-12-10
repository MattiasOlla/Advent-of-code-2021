import re
from collections import defaultdict
from pathlib import Path

filepath = Path(__file__)
data_path = filepath.parent / "data.txt"

pattern = re.compile(R"^(\d+),(\d+) -> (\d+),(\d+)$")

lines = data_path.read_text().splitlines()
print(len([l for l in lines if l]))
coords = [[int(num) for num in re.match(pattern, line).groups()] for line in lines]
print(len(coords))


def line_points(
    x0: int, y0: int, x1: int, y1: int, *, include_diagonals: bool
) -> list[tuple[int, int]]:
    if x0 == x1:
        start, stop = min(y0, y1), max(y0, y1)
        return [(x0, y) for y in range(start, stop + 1)]
    elif y0 == y1:
        start, stop = min(x0, x1), max(x0, x1)
        return [(x, y0) for x in range(start, stop + 1)]

    if include_diagonals:
        print(f"Skipping coords {(x0, y0)}, {(y0, y1)}")
        return []

    if x0 - x1 == y0 - y1:
        (x_start, y_start), (x_stop, y_stop) = min((x0, y0), (x1, y1)), max((x0, y0), (x1, y1))
        return [(x_start + i, y_start + i) for i in range(0, x_stop - x_start + 1)]
    elif x0 - x1 == y1 - y0:
        (x_start, y_start), (x_stop, y_stop) = min((x0, y0), (x1, y1)), max((x0, y0), (x1, y1))
        return [(x_start + i, y_start - i) for i in range(0, x_stop - x_start + 1)]
    raise ValueError("Bläää")


def solution(include_diagonals: bool):
    counts = defaultdict(int)
    for line_start_stop_coords in coords:
        line_coords = line_points(*line_start_stop_coords, include_diagonals=include_diagonals)
        print(
            f"Start: {line_start_stop_coords[:2]}, stop: {line_start_stop_coords[2:]}, coords:"
            f" {line_coords}\n"
        )
        for coord in line_coords:
            counts[coord] += 1

    points_with_more_than_two = [(point, count) for point, count in counts.items() if count >= 2]
    # for point in points_with_more_than_two:
    #     print(point)

    print(f"Number of points with more than one line: {len(points_with_more_than_two)}")


def part1():
    solution(False)


def part2():
    solution(False)


if __name__ == "__main__":
    part1()
    part2()
