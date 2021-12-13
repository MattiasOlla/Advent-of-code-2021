from pathlib import Path
from typing import Literal, TypeAlias

DataType: TypeAlias = tuple[list[tuple[int, int]], list[tuple[Literal["x", "y"], int]]]

data_path = Path(__file__).parent / "data.txt"


def parse_data(text: str) -> DataType:
    print(text)
    coords_str, instructions_str = text.split("\n\n")
    coords = [
        (int(x), int(y)) for line in coords_str.splitlines() for x, _, y in [line.partition(",")]
    ]
    instructions = [
        (dim, int(coord))
        for line in instructions_str.splitlines()
        for dim, _, coord in [line.split()[-1].partition("=")]
    ]
    return coords, instructions  # type: ignore


def fold(
    coords: set[tuple[int, int]], dim: Literal["x", "y"], fold_coord: int
) -> set[tuple[int, int]]:
    folded = set()
    for x, y in coords:
        match dim:
            case "x":
                folded.add((2 * fold_coord - x, y) if x > fold_coord else (x, y))
            case "y":
                folded.add((x, 2 * fold_coord - y) if y > fold_coord else (x, y))
    return folded


def coords_repr(coords: set[tuple[int, int]]) -> str:
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)
    return "\n".join(
        "".join("#" if (x, y) in coords else "." for x in range(max_x + 1))
        for y in range(max_y + 1)
    )


def part1(data: DataType) -> int:
    coords, instructions = data
    coords_set = set(coords)
    first_fold = fold(coords_set, *instructions[0])
    return len(first_fold)


def part2(data: DataType) -> str:
    coords, instructions = data
    coords_set = set(coords)
    for instruction in instructions:
        coords_set = fold(coords_set, *instruction)
    return coords_repr(coords_set)


if __name__ == "__main__":
    data = parse_data(data_path.read_text())
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result:\n{part2(data)}")
