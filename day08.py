from dataclasses import dataclass
import logging

logger = logging.Logger(__name__)


@dataclass
class Point:
    y: int
    x: int

    def __lt__(self, other) -> bool:
        if self.y < other.y:
            return True

        if self.y > other.y:
            return False

        if self.x < other.x:
            return True

        return False


def find_matching_points(data: list[str], point: Point):
    search = data[point.y][point.x]

    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            # skip earlier points as we'll have already done them
            if y < point.y:
                continue
            elif y == point.y and x < point.x:
                continue

            # don't match against the same point!
            if y == point.y and x == point.x:
                continue

            if search == ch:
                yield Point(y, x)


def find_antipodes(data: list[str], p1: Point, p2: Point) -> list[Point]:
    yd = abs(p1.y - p2.y)
    xd = abs(p1.x - p2.x)

    result = []

    logging.debug("%s - %s", p1, p2)

    def _find_antipodes_one_way(a: Point, b: Point):
        if a.y <= b.y:
            if a.x <= b.x:
                if a.y - yd >= 0 and a.x - xd >= 0:
                    antipode = Point(a.y - yd, a.x - xd)
                    logging.debug("  %s", antipode)
                    yield antipode
            else:
                if a.y - yd >= 0 and a.x + xd < len(data[0]):
                    antipode = Point(a.y - yd, a.x + xd)
                    logging.debug("  %s", antipode)
                    yield antipode
        else:
            if a.x <= b.x:
                if a.y + yd < len(data) and a.x - xd >= 0:
                    antipode = Point(a.y + yd, a.x - xd)
                    logging.debug("  %s", antipode)
                    yield antipode
            else:
                if a.y + yd < len(data) and a.x + xd < len(data[0]):
                    antipode = Point(a.y + yd, a.x + xd)
                    logging.debug("  %s", antipode)
                    yield antipode

    for antipode in _find_antipodes_one_way(p1, p2):
        result.append(antipode)
    for antipode in _find_antipodes_one_way(p2, p1):
        result.append(antipode)

    return result


def func1(data: list[str]):
    result = []
    for y, line in enumerate(data):
        for x in range(len(line)):
            # Only interested in antennas
            if data[y][x] in '.#':
                continue

            ant = Point(y,x)

            # Find the matching points
            for other in find_matching_points(data, ant):
                for antipode in find_antipodes(data, ant, other):
                    if antipode not in result:
                        result.append(antipode)

    return len(result)
