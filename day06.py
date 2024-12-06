from dataclasses import dataclass
from enum import Enum

print("..loading day06")

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

@dataclass
class Point:
    y: int
    x: int

    def move(self, dir: Direction) -> "Point":
        return Point(self.y+dir.value[0],self.x+dir.value[1])

def get_point_on_map(data: list[str], point: Point) -> str | None:
    if point.x < 0 or point.y < 0:
        return None

    if point.y >= len(data) or point.x >= len(data[0]):
        return None

    return data[point.y][point.x]

direction_map = {
    "^": Direction.UP,
    ">": Direction.RIGHT,
    "v": Direction.DOWN,
    "<": Direction.LEFT,
}

turn_map = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}

def find_guard(data: list[str]) -> Point:
    for i, line in enumerate(data):
        for j, ch in enumerate(line):
            if ch in "^><v":
                return Point(i,j)

    raise ValueError("could not find guard!")

def get_next_pos(data: list[str], pos: Point, dir: Direction) -> tuple[Point, Direction] | None:
    for _ in range(4):
        next_pos = pos.move(dir)
        if not get_point_on_map(data, next_pos):
            return None

        ch = data[next_pos.y][next_pos.x]
        if ch != '#':
            return (next_pos, dir)

        dir = turn_map[dir]

    raise ValueError('could not find safe turn')


def func1(data: list[str]):
    visited: list[Point] = []

    pos = find_guard(data)
    print(f"found guard: {pos} = {data[pos.y][pos.x]}")
    visited.append(pos)
    dir = direction_map[data[pos.y][pos.x]]

    while True:
        result = get_next_pos(data, pos, dir)
        if result is None:
            break

        next_pos, dir = result
        if next_pos not in visited:
            visited.append(next_pos)

        pos = next_pos

    return len(visited)
