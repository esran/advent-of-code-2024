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

    def __hash__(self):
        return hash(f"{self.y}.{self.x}")

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

reverse_direction_map = {
    Direction.UP: "^",
    Direction.DOWN: "v",
    Direction.LEFT: "<",
    Direction.RIGHT: ">",
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

def walk_route(data: list[str], pos: Point, dir: Direction) -> tuple[dict[Point, str], bool]:
    visited: dict[Point, str] = {}

    # print(f"start: {pos} {dir}")
    visited[pos] = '|' if dir in [Direction.UP, Direction.DOWN] else '-'

    while True:
        next_pos = pos.move(dir)
        ch = reverse_direction_map[dir]
        if not get_point_on_map(data, next_pos):
            # print("end off map")
            return visited, False

        # If we've already visited this spot then check if it was
        # in this direction, in which case we've looped.
        if next_pos in visited:
            if ch in visited[next_pos]:
                # print(f"end looped {next_pos} {visited[next_pos]}")
                return visited, True

            visited[next_pos] += ch
            # print(f"{ch} {next_pos}  {visited[next_pos]}")
            pos = next_pos
            continue


        # If this isn't an obstacle visit it and carry on
        if data[next_pos.y][next_pos.x] != '#':
            # print(f"{ch} {next_pos}")
            visited[next_pos] = ch
            pos = next_pos
            continue

        # Turn
        # print("  turn")
        dir = turn_map[dir]

def func1(data: list[str]):
    visited: dict[Point, str] = {}

    pos = find_guard(data)
    dir = direction_map[data[pos.y][pos.x]]

    visited, loop = walk_route(data, pos, dir)
    # print(f"loop: {loop}")

    return len(visited)

def func2(data: list[str]):
    visited: dict[Point, str] = {}

    start_pos = find_guard(data)
    start_dir = direction_map[data[start_pos.y][start_pos.x]]

    pos, dir = start_pos, start_dir
    visited, _ = walk_route(data, pos, dir)

    result = 0

    # Iterate over the visited places that aren't adjacent to the
    # start position making a new map with a # at the place and
    # see if that results in a loop (update_visited returns True)

    for i, check_pos in enumerate(visited.keys()):
        # can't place on the start pos
        if check_pos == start_pos:
            continue

        new_data = data.copy()
        new_data[check_pos.y] = data[check_pos.y][0:check_pos.x] + '#' + data[check_pos.y][check_pos.x+1:]

        pos, dir = start_pos, start_dir
        _, loop = walk_route(new_data, pos, dir)

        if loop:
            result += 1

    return result
