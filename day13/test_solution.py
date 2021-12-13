from textwrap import dedent

from .solution import parse_data, part1, part2

test_data_text = dedent(
    """
    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5
    """
).strip()
print(test_data_text)
test_data = parse_data(test_data_text)


def test_part1():
    assert part1(test_data) == 17


def test_part2():
    expected = dedent(
        """
        #####
        #...#
        #...#
        #...#
        #####
        """
    ).strip()

    recieved = part2(test_data)

    assert expected == recieved
