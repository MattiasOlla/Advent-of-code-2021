from textwrap import dedent
from typing import Counter

from .solution import find_paths, find_paths_allow_one_twice, parse_data, part1, part2

test_data_str = dedent(
    """
    dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc
    """
).strip()
test_data = parse_data(test_data_str)

test_data_str_short = dedent(
    """
    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end
    """
).strip()
test_data_short = parse_data(test_data_str_short)


test_data_long = parse_data(
    dedent(
        """
        fs-end
        he-DX
        fs-he
        start-DX
        pj-DX
        end-zg
        zg-sl
        zg-pj
        pj-he
        RW-he
        fs-DX
        pj-RW
        zg-RW
        start-pj
        he-WI
        zg-he
        pj-fs
        start-RW
        """
    ).strip()
)


def test_find_paths():
    paths = set(str(p) for p in find_paths(test_data))
    assert paths == {
        "start,HN,dc,HN,end",
        "start,HN,dc,HN,kj,HN,end",
        "start,HN,dc,end",
        "start,HN,dc,kj,HN,end",
        "start,HN,end",
        "start,HN,kj,HN,dc,HN,end",
        "start,HN,kj,HN,dc,end",
        "start,HN,kj,HN,end",
        "start,HN,kj,dc,HN,end",
        "start,HN,kj,dc,end",
        "start,dc,HN,end",
        "start,dc,HN,kj,HN,end",
        "start,dc,end",
        "start,dc,kj,HN,end",
        "start,kj,HN,dc,HN,end",
        "start,kj,HN,dc,end",
        "start,kj,HN,end",
        "start,kj,dc,HN,end",
        "start,kj,dc,end",
    }


def test_find_paths_allowed_twice_short():
    paths = list(find_paths_allow_one_twice(test_data_short))
    paths_str = set(str(p) for p in paths)
    expected = {
        "start,A,b,A,b,A,c,A,end",
        "start,A,b,A,b,A,end",
        "start,A,b,A,b,end",
        "start,A,b,A,c,A,b,A,end",
        "start,A,b,A,c,A,b,end",
        "start,A,b,A,c,A,c,A,end",
        "start,A,b,A,c,A,end",
        "start,A,b,A,end",
        "start,A,b,d,b,A,c,A,end",
        "start,A,b,d,b,A,end",
        "start,A,b,d,b,end",
        "start,A,b,end",
        "start,A,c,A,b,A,b,A,end",
        "start,A,c,A,b,A,b,end",
        "start,A,c,A,b,A,c,A,end",
        "start,A,c,A,b,A,end",
        "start,A,c,A,b,d,b,A,end",
        "start,A,c,A,b,d,b,end",
        "start,A,c,A,b,end",
        "start,A,c,A,c,A,b,A,end",
        "start,A,c,A,c,A,b,end",
        "start,A,c,A,c,A,end",
        "start,A,c,A,end",
        "start,A,end",
        "start,b,A,b,A,c,A,end",
        "start,b,A,b,A,end",
        "start,b,A,b,end",
        "start,b,A,c,A,b,A,end",
        "start,b,A,c,A,b,end",
        "start,b,A,c,A,c,A,end",
        "start,b,A,c,A,end",
        "start,b,A,end",
        "start,b,d,b,A,c,A,end",
        "start,b,d,b,A,end",
        "start,b,d,b,end",
        "start,b,end",
    }
    assert paths_str == expected


def test_find_paths_allowed_twice():
    paths = list(find_paths_allow_one_twice(test_data))
    # for path in paths:
    #     print(path)
    #     print(Counter([c.name for c in path.path]))
    # print(len(set("".join(sorted(c.name for c in path.path)) for path in paths)))
    assert len(paths) == 103


def test_find_paths_allowed_twice_long():
    paths = list(find_paths_allow_one_twice(test_data_long))
    for path in paths:
        print(Counter([c.name for c in path.path]))

    assert len(set(paths)) == 3509


def test_part1():
    assert part1(test_data) == 19


def test_part2():
    assert part2(test_data) == 103
