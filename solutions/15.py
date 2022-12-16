from __future__ import annotations
import re


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other: Pos):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Pos(self.x * other, self.y * other)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def rounded(self):
        return Pos(round(self.x), round(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def load():
    sensors: dict[Pos, Pos] = {}
    for line in open("15_input.txt"):
        match = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)\n", line)
        sensors[Pos(int(match.group(1)), int(match.group(2)))] = Pos(int(match.group(3)), int(match.group(4)))
    return sensors


# sort in place
def merge_intervals(intervals: list[tuple[int, int]]):
    intervals.sort(key=lambda x: x[0])

    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] < intervals[i + 1][1]:
                intervals[i] = (intervals[i][0], intervals[i + 1][1])
            intervals.pop(i + 1)
        else:
            i += 1


def get_cleared(sensors: dict[Pos, Pos], row: int):
    ranges = []
    for sensor, beacon in sensors.items():
        distance = sensor.distance(beacon)
        radius = distance - abs(sensor.y - row)
        if radius >= 0:
            min = sensor.x - radius
            max = sensor.x + radius + 1
            ranges.append((min, max))

    merge_intervals(ranges)
    return sum([i[1] - i[0] - 1 for i in ranges])


def part1():
    sensors = load()
    print(get_cleared(sensors, 20))


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2}) <{self.gradient()}>"

    def gradient(self):
        return (self.y2 - self.y1)//(self.x2 - self.x1)

    def intersection(self, other: Line) -> Pos | None:
        m1 = self.gradient()
        m2 = other.gradient()
        if m1 == m2:
            return None
        c1 = self.y1 - (self.x1 * m1)
        c2 = other.y1 - (other.x1 * m2)
        x = (c2 - c1) // (m1 - m2)
        if self.x1 <= x <= self.x2 and other.x1 <= x <= other.x2:
            return Pos(x, m1 * x + c1)
        else:
            return None


def part2():
    sensors = load()
    lines = []
    max_range = 4_000_000
    for sensor, beacon in sensors.items():
        distance = sensor.distance(beacon)
        lines.append(Line(sensor.x + distance + 1, sensor.y, sensor.x + 1, sensor.y - distance))
        lines.append(Line(sensor.x, sensor.y - distance - 1, sensor.x - distance, sensor.y - 1))
        lines.append(Line(sensor.x - distance - 1, sensor.y, sensor.x - 1, sensor.y + distance))
        lines.append(Line(sensor.x, sensor.y + distance + 1, sensor.x + distance, sensor.y + 1))

    to_check = set()
    for i in range(len(lines)):
        for j in range(1, len(lines)):
            line = lines[i]
            other_line = lines[j]
            if line != other_line:
                intersection = line.intersection(other_line)
                if intersection is not None:
                    if 0 <= intersection.x <= max_range and 0 <= intersection.y <= max_range:
                        to_check.add(intersection)

    point = None
    for point in to_check:
        invalid = False
        for sensor, beacon in sensors.items():
            if sensor.distance(point) <= sensor.distance(beacon):
                invalid = True
                break
        if not invalid:
            break
    assert point is not None
    print(4_000_000 * point.x + point.y)


part1()
part2()
