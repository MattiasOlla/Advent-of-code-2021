from pathlib import Path

data_path = Path(__file__).parent / "data.txt"
instructions = [line.split() for line in data_path.read_text().splitlines()]


def part1():
    instruction_map = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}

    position = (0, 0)
    for direction, distance in instructions:
        position = tuple(
            int(distance) * x + p for x, p in zip(instruction_map[direction], position)
        )

    print(f"Final position: {position}")
    print(f"Product: {position[0] * position[1]}")


def part2():
    aim = 0
    position = (0, 0)

    for direction, num in instructions:
        num = int(num)
        match direction:
            case "forward":
                position = (position[0] + num, position[1] + aim * num)
            case "up":
                aim -= num
            case "down":
                aim += num

    print(f"Final position: {position}")
    print(f"Product: {position[0] * position[1]}")


if __name__ == "__main__":
    print("Part 1:")
    part1()
    print("\n\nPart 2:")
    part2()
