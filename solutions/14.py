import math
import re


def sign(x: int):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def load() -> (dict[int, dict[int, str]], tuple[int, int], tuple[int, int]):
    grid = {
        0: {
            500: "+"
        }
    }

    lowest_x = 1_000_000
    lowest_y = 0
    highest_x = -1_000_000
    highest_y = -1_000_000

    def mark_grid(x_pos, y_pos):
        nonlocal lowest_x, lowest_y, highest_x, highest_y

        if y_pos not in grid:
            grid[y_pos] = {}
        grid[y_pos][x_pos] = "#"

        lowest_x = min(lowest_x, x_pos)
        lowest_y = min(lowest_y, y_pos)
        highest_x = max(highest_x, x_pos)
        highest_y = max(highest_y, y_pos)

    for line in open("14_input.txt"):
        points = []
        for point_str in line[:-1].split(" -> "):
            coords = point_str.split(",")
            points.append((int(coords[0]), int(coords[1])))

        for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
            if x1 != x2:
                x_sign = sign(x2 - x1)
                for x in range(x1, x2 + x_sign, x_sign):
                    mark_grid(x, y1)
            else:
                y_sign = sign(y2 - y1)
                for y in range(y1, y2 + y_sign, y_sign):
                    mark_grid(x1, y)

    return grid, (lowest_x, lowest_y), (highest_x, highest_y)


def print_grid(grid, lowest_x, lowest_y, highest_x, highest_y):
    s = ""
    for y in range(lowest_y, highest_y + 1):
        for x in range(lowest_x, highest_x + 1):
            if y in grid and x in grid[y]:
                s += grid[y][x] + " "
            else:
                s += ". "
        s += "\n"
    print(s)


# simulates sand in place
def simulate_sand(grid, cutoff):
    sand_settled = 0
    more_sand = True
    while more_sand:
        sand_x = 500
        sand_y = 0
        sand_moving = True
        while sand_moving:
            if sand_y + 1 not in grid or sand_x not in grid[sand_y + 1]:
                sand_y += 1
                if sand_y > cutoff:
                    sand_moving = False
                    more_sand = False
            elif sand_x - 1 not in grid[sand_y + 1]:
                sand_y += 1
                sand_x -= 1
            elif sand_x + 1 not in grid[sand_y + 1]:
                sand_y += 1
                sand_x += 1
            else:
                if sand_y not in grid:
                    grid[sand_y] = {}
                grid[sand_y][sand_x] = "o"
                sand_moving = False
                sand_settled += 1

                if sand_x == 500 and sand_y == 0:
                    more_sand = False
    return sand_settled


def part1():
    grid, (lowest_x, lowest_y), (highest_x, highest_y) = load()
    settled = simulate_sand(grid, highest_y)
    #print_grid(grid, lowest_x, lowest_y, highest_x, highest_y)
    print(settled)


def part2():
    grid, (lowest_x, lowest_y), (highest_x, highest_y) = load()

    highest_y += 2
    lowest_x = min(lowest_x - 2, 500 - highest_y)
    highest_x = max(highest_x + 2, 500 + highest_y)
    grid[highest_y] = {}
    grid[highest_y - 1] = {}
    for x in range(-highest_y + 500, highest_y + 501):
        grid[highest_y][x] = "#"
    #print_grid(grid, lowest_x, lowest_y, highest_x, highest_y)
    settled = simulate_sand(grid, highest_y)
    #print_grid(grid, lowest_x, lowest_y, highest_x, highest_y)
    print(settled)


part1()
part2()
