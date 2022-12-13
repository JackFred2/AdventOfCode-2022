import re


def sign(i: int):
    if i == 0:
        return 0
    elif i > 0:
        return 1
    else:
        return -1


def part1():
    with open("09_input.txt") as f:
        head_x = 0
        head_y = 0
        tail_x = 0
        tail_y = 0

        tail_positions = set()
        tail_positions.add((tail_x, tail_y))
        instructions = []

        for instruction_lines in f.readlines():
            direction = instruction_lines[0]
            distance = int(instruction_lines[2:-1])
            for _ in range(distance):
                instructions.append(direction)

        for instruction in instructions:
            match instruction:
                case "R":
                    head_x += 1
                case "L":
                    head_x -= 1
                case "U":
                    head_y += 1
                case "D":
                    head_y -= 1
            x_offset = head_x - tail_x
            y_offset = head_y - tail_y
            if abs(x_offset) <= 1 and abs(y_offset) <= 1:  # no movement
                continue
            else:
                if abs(x_offset) == 2:
                    tail_x += sign(x_offset)
                    tail_y = head_y
                elif abs(y_offset) == 2:
                    tail_y += sign(y_offset)
                    tail_x = head_x
            tail_positions.add((tail_x, tail_y))

        print(len(tail_positions))


def part2():
    instructions = []
    positions = [(0, 0)] * 10
    tail_positions = set()
    tail_positions.add((0, 0))

    min_x = -10
    max_x = 10
    min_y = -10
    max_y = 10

    def get_new_pos(current_head_pos: tuple[int, int], current_tail_pos: tuple[int, int]) -> tuple[int, int]:
        x_offset = current_head_pos[0] - current_tail_pos[0]
        y_offset = current_head_pos[1] - current_tail_pos[1]
        if abs(x_offset) <= 1 and abs(y_offset) <= 1:  # no movement
            return current_tail_pos
        else:
            if abs(x_offset) == abs(y_offset) == 2:
                return current_tail_pos[0] + sign(x_offset), current_tail_pos[1] + sign(y_offset)
            elif abs(x_offset) == 2:
                return current_tail_pos[0] + sign(x_offset), current_head_pos[1]
            elif abs(y_offset) == 2:
                return current_head_pos[0], current_tail_pos[1] + sign(y_offset)

    with open("09_input.txt") as f:
        for instruction_lines in f.readlines():
            direction = instruction_lines[0]
            distance = int(instruction_lines[2:-1])
            for _ in range(distance):
                instructions.append(direction)

    for instruction in instructions:
        head_pos = positions[0]
        match instruction:
            case "R":
                head_pos = (head_pos[0] + 1, head_pos[1])
            case "L":
                head_pos = (head_pos[0] - 1, head_pos[1])
            case "U":
                head_pos = (head_pos[0], head_pos[1] + 1)
            case "D":
                head_pos = (head_pos[0], head_pos[1] - 1)
        positions[0] = head_pos
        min_x = min(min_x, head_pos[0])
        min_y = min(min_y, head_pos[1])
        max_x = max(max_x, head_pos[0])
        max_y = max(max_y, head_pos[1])

        for i in range(1, 10):
            head_pos = positions[i - 1]
            tail_pos = positions[i]
            new_tail_pos = get_new_pos(head_pos, tail_pos)
            if tail_pos != new_tail_pos:
                positions[i] = new_tail_pos
            else:
                break

        # strs = []
        # for y in range(max_y + 1 - min_y):
        #     strs.append([])
        #     for x in range(max_x + 1 - min_x):
        #         strs[y].append(". ")
        # for pos in positions:
        #     strs[pos[1] - min_y][pos[0] - min_x] = "# "
        # strs.reverse()
        # strs[min_y - 1][min_x - 1] = "s "
        # print("\n".join(["".join(t) for t in strs]) + "\n")

        tail_positions.add(positions[9])
    print(len(tail_positions))


part1()
part2()
