import re


def part1():
    with open("5_input.txt") as f:
        stacks = []
        stack_count = len(f.readline()) // 4
        f.seek(0)
        for _ in range(stack_count):
            stacks.append([])

        # read initial state
        while True:
            line = f.readline()
            if line[1].isdigit():  # digit line
                break
            for i in range(stack_count):
                slot = line[4 * i:4 * i + 3]
                if slot != "   ":
                    stacks[i].append(slot[1])

        f.readline()  # blank

        # read moves
        while True:
            line = f.readline()
            if line == "":
                break
            match = re.search("move (\\d+) from (\\d) to (\\d)", line)
            count = int(match.group(1))
            from_stack = int(match.group(2)) - 1
            to_stack = int(match.group(3)) - 1
            for i in range(count):
                stacks[to_stack].insert(0, stacks[from_stack].pop(0))

        result = ""
        for stack in stacks:
            result += stack[0]
        print(result)


def part2():
    with open("5_input.txt") as f:
        stacks = []
        stack_count = len(f.readline()) // 4
        f.seek(0)
        for _ in range(stack_count):
            stacks.append([])

        # read initial state
        while True:
            line = f.readline()
            if line[1].isdigit():  # digit line
                break
            for i in range(stack_count):
                slot = line[4 * i:4 * i + 3]
                if slot != "   ":
                    stacks[i].append(slot[1])

        f.readline()  # blank

        # read moves
        while True:
            line = f.readline()
            if line == "":
                break
            match = re.search("move (\\d+) from (\\d) to (\\d)", line)
            count = int(match.group(1))
            from_stack = int(match.group(2)) - 1
            to_stack = int(match.group(3)) - 1
            hooked = stacks[from_stack][:count]
            stacks[from_stack] = stacks[from_stack][count:]
            stacks[to_stack] = hooked + stacks[to_stack]

        result = ""
        for stack in stacks:
            result += stack[0]
        print(result)


part1()
part2()
