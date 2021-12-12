from textwrap import dedent

from .solution import Grid, parse_data, part1, part2

test_data_str1 = dedent(
    """
    11111
    19991
    19191
    19991
    11111

    34543
    40004
    50005
    40004
    34543

    45654
    51115
    61116
    51115
    45654
    """
)
grids = [Grid(s) for s in test_data_str1.split("\n\n")]
test_str = dedent(
    """
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    """
).strip()


def test_grid():
    grids[0].step()
    assert grids[0].energy_levels() == grids[1].energy_levels()
    grids[0].step()
    assert grids[0].energy_levels() == grids[2].energy_levels()


def test_part1():
    assert part1(test_str) == 1656


def test_part2() -> int:
    return part2(test_str) == 195
