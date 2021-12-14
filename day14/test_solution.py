from textwrap import dedent

import pytest

from .solution import increment_polymer, parse_data, part1, part2

test_data = parse_data(
    dedent(
        """
        NNCB

        CH -> B
        HH -> N
        CB -> H
        NH -> C
        HB -> C
        HC -> B
        HN -> C
        NN -> C
        BH -> H
        NC -> B
        NB -> B
        BN -> B
        BB -> N
        BC -> B
        CC -> N
        CN -> C
        """
    ).strip()
)


def test_increment_polymer():
    polymer, rules = test_data
    assert increment_polymer(polymer, rules) == "NCNBCHB"
    assert increment_polymer("NCNBCHB", rules) == "NBCCNBBBCBHCB"
    assert increment_polymer("NBCCNBBBCBHCB", rules) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    assert (
        increment_polymer("NBBBCNCCNBBNBNBBCHBHHBCHB", rules)
        == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )


def test_part1():
    expected = 1588
    result = part1(test_data)
    assert result == expected


@pytest.mark.timeout(10)
def test_part2():
    expected = 2188189693529
    result = part2(test_data)
    assert result == expected
