from pathlib import Path

data_path = Path(__file__).parent / "data" / "day4.txt"


class Board:
    def __init__(self, board_text: str) -> None:
        lines = board_text.splitlines()
        self.size = len(lines)  # Assume square board
        self.numbers = [int(x) for line in lines for x in line.split()]
        self.marked: set[tuple[int, int]] = set()

    def mark(self, num: int) -> None:
        try:
            index = self.numbers.index(num)
        except ValueError:
            return
        self.marked.add(self.get_coord(index))

    def get_coord(self, index: int) -> tuple[int, int]:
        return (index // self.size, index % self.size)

    def bingo(self) -> bool:
        for row in range(self.size):
            if all((row, i) in self.marked for i in range(self.size)):
                return True

        for col in range(self.size):
            if all((i, col) in self.marked for i in range(self.size)):
                return True

        return False

    def sum_unmarked(self) -> int:
        return sum(
            num
            for index, num in enumerate(self.numbers)
            if self.get_coord(index) not in self.marked
        )


data = data_path.read_text()
numbers_str, *boards_str = data.split("\n\n")
numbers = [int(x) for x in numbers_str.split(",")]
boards = [Board(b_str) for b_str in boards_str]


def part1():
    for number in numbers:
        print(f"Marking number {number}")
        for board_num, board in enumerate(boards):
            board.mark(number)
            if board.bingo():
                print(f"Board {board_num} won!")
                sum_unmarked = board.sum_unmarked()
                print(f"Sum of unmarked numbers: {sum_unmarked}")
                final_score = number * sum_unmarked
                print(f"Final score: {final_score}")
                return


def part2():
    boards_won = set()
    for number in numbers:
        print(f"Marking number {number}")
        for board_num, board in enumerate(boards):
            if board_num in boards_won:
                continue

            board.mark(number)
            if board.bingo():
                boards_won.add(board_num)
                print(f"Board {board_num} won!")
                sum_unmarked = board.sum_unmarked()
                final_score = number * sum_unmarked
                print(f"Final score for board {board_num}: {final_score}")


if __name__ == "__main__":
    part1()
    print()
    part2()
