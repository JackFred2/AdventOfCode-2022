import re

pattern = "^(\\d+)-(\\d+),(\\d+)-(\\d+)\n$"


def part1():
    total = 0

    with open("4_input.txt") as f:
        for line in f.readlines():
            match = re.search(pattern, line)
            first_start = int(match.group(1))
            first_end = int(match.group(2))
            second_start = int(match.group(3))
            second_end = int(match.group(4))
            if first_start <= second_start and second_end <= first_end or second_start <= first_start and first_end <= second_end:
                total += 1
    print(total)


def part2():
    total = 0

    with open("4_input.txt") as f:
        for line in f.readlines():
            match = re.search(pattern, line)
            first_start = int(match.group(1))
            first_end = int(match.group(2))
            second_start = int(match.group(3))
            second_end = int(match.group(4))
            if first_end >= second_start and second_end >= first_start:
                total += 1
    print(total)


part1()
part2()
