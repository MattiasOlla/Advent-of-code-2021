from datetime import date
from pathlib import Path
from string import Template
from textwrap import dedent
from typing import Optional

import typer

solution = Template(
    dedent(
        """
        from pathlib import Path
        from typing import Any, TypeAlias

        DataType: TypeAlias = Any

        data_path = Path(__file__).parent / "data.txt"


        def parse_data(text: str) -> DataType:
            return text


        def part1(data: DataType) -> int:
            return 0


        def part2(data: DataType) -> int:
            return 0


        if __name__ == "__main__":
            data = parse_data(data_path.read_text())
            print(f"Part 1 result: {part1(data)}")
            print(f"Part 2 result: {part2(data)}")
        """
    ).lstrip()
)


test = Template(
    dedent(
        '''
        from textwrap import dedent

        from .solution import parse_data, part1, part2

        test_data = parse_data(
            dedent(
                """

                """
            ).strip()
        )


        def test_part1():
            assert part1(test_data) == 0


        def test_part2() -> int:
            return part2(test_data) == 0
        '''
    ).lstrip()
)


def main(day_num: Optional[int] = None) -> None:
    folder = make_day_folder(day_num or date.today().day)
    (folder / "data.txt").touch()
    (folder / "solution.py").write_text(solution.substitute())
    (folder / "test_solution.py").write_text(test.substitute())
    (folder / "__init__.py").write_text(test.substitute())


def make_day_folder(day_num: int) -> Path:
    folder = Path(__file__).parent / f"day{day_num}"
    folder.mkdir()
    return folder


if __name__ == "__main__":
    typer.run(main)
