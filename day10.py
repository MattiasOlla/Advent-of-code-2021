from collections.abc import Generator
from enum import Enum
from pathlib import Path
from textwrap import dedent

filepath = Path(__file__)
data_path = filepath.parent / "data" / f"{filepath.stem}.txt"
data = data_path.read_text().splitlines()


class LineResult(str, Enum):
    OK = "OK"
    INCOMPLETE = "INCOMPLETE"
    CORRUPTED = "CORRUPTED"


OPEN_CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSE_OPEN = {v: k for k, v in OPEN_CLOSE.items()}


CORRUPTED_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def line_result(line: str) -> tuple[LineResult, str]:
    char_stack = []
    for char in line:
        if char in OPEN_CLOSE:
            char_stack.append(char)
        elif OPEN_CLOSE[char_stack.pop()] != char:
            return LineResult.CORRUPTED, char

    if char_stack:
        return LineResult.INCOMPLETE, "".join(char_stack)

    return LineResult.OK, ""


def part1(lines: list[str]):
    score = 0
    for line in lines:
        result, illegal_or_incomplete = line_result(line)
        if result == LineResult.CORRUPTED:
            score += CORRUPTED_POINTS[illegal_or_incomplete]
    print(f"Error score: {score}")


def autocomplete_gen(lines: list[str]) -> Generator[int, None, None]:
    for line in lines:
        result, illegal_or_incomplete = line_result(line)
        if result == LineResult.INCOMPLETE:
            score = 0
            for char in reversed(illegal_or_incomplete):
                score = score * 5 + INCOMPLETE_POINTS[OPEN_CLOSE[char]]
            print(f"Incomplete: {illegal_or_incomplete}, score: {score}")
            yield score


def part2(lines: list[str]):
    scores = list(autocomplete_gen(lines))
    assert len(scores) % 2 == 1
    middle_score = sorted(scores)[len(scores) // 2]
    print(f"Autocomplete middle score: {middle_score}")


if __name__ == "__main__":
    test = dedent(
        """
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]
        """
    ).splitlines()
    part1(data)
    part2(data)
