from textwrap import dedent
from typing import Counter

import pytest

from .solution import count_pairs, parse_data, part1, part2

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


def test_count_pairs():
    polymer, rules = test_data
    assert count_pairs(polymer, rules, 1) == Counter(
        {
            (" ", "N"): 1,
            ("N", "C"): 1,
            ("C", "N"): 1,
            ("N", "B"): 1,
            ("B", "C"): 1,
            ("C", "H"): 1,
            ("H", "B"): 1,
            ("B", " "): 1,
        }
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
