from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, TypeAlias

DataType: TypeAlias = dict[str, "Cave"]

data_path = Path(__file__).parent / "data.txt"


@dataclass
class Cave:
    name: str
    small: bool

    neighbours: list["Cave"] = field(default_factory=list)

    @classmethod
    def from_name(cls, name: str) -> "Cave":
        return cls(name=name, small=name.islower())


def parse_data(text: str) -> DataType:
    caves = {}
    for line in text.splitlines():
        name1, _, name2 = line.partition("-")
        cave1 = caves.setdefault(name1, Cave.from_name(name1))
        cave2 = caves.setdefault(name2, Cave.from_name(name2))
        cave1.neighbours.append(cave2)
        cave2.neighbours.append(cave1)
    return caves


class CavePath:
    def __init__(self, path: list[Cave], visited: defaultdict[str, int] | None = None) -> None:
        self.path: list[Cave] = path
        if visited:
            self.visited = visited
        else:
            self.visited: defaultdict[str, int] = defaultdict(int)
            for cave in self.path:
                if cave.small:
                    self.visited[cave.name] += 1

        self.allowed_twice = ""

    @property
    def last(self) -> Cave:
        return self.path[-1]

    def append(self, cave: Cave) -> None:
        self.path.append(cave)
        if cave.small:
            self.visited[cave.name] += 1

    def __str__(self) -> str:
        return ",".join(cave.name for cave in self.path)

    def copy(self) -> "CavePath":
        new = CavePath(self.path.copy(), visited=self.visited.copy())
        new.allowed_twice = self.allowed_twice
        return new


def find_paths(
    caves: dict[str, Cave],
    start_name: str = "start",
    end_name: str = "end",
) -> Generator[CavePath, None, None]:
    queue = deque([CavePath([caves[start_name]])])
    while queue:
        curr = queue.popleft()
        if curr.last.name == end_name:
            yield curr
            continue
        for neighbour in curr.last.neighbours:
            times_visited = curr.visited.get(neighbour.name, 0)
            if times_visited == 0:
                new = curr.copy()
                new.append(neighbour)
                queue.append(new)


def find_paths_allow_one_twice(
    caves: dict[str, Cave],
    start_name: str = "start",
    end_name: str = "end",
) -> Generator[CavePath, None, None]:
    queue = deque([CavePath([caves[start_name]])])
    while queue:
        curr = queue.popleft()
        if curr.last.name == end_name:
            yield curr
            continue
        for neighbour in curr.last.neighbours:
            times_visited = curr.visited.get(neighbour.name, 0)
            if times_visited == 0 or (
                times_visited == 1
                and not curr.allowed_twice
                and neighbour.name not in {start_name, end_name}
            ):
                new = curr.copy()
                if times_visited == 1:
                    new.allowed_twice = neighbour.name
                new.append(neighbour)
                queue.append(new)


def part1(data: DataType) -> int:
    return len(list(find_paths(data)))


def part2(data: DataType) -> int:
    return len(set(find_paths_allow_one_twice(data)))


if __name__ == "__main__":
    data = parse_data(data_path.read_text())
    print(f"Part 1 result: {part1(data)}")
    print(f"Part 2 result: {part2(data)}")
