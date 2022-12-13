def part1():
    with open("10_input.txt") as f:
        register = 1
        register_values = []
        for line in f.readlines():
            if line.startswith("noop"):
                register_values.append(register)
            elif line.startswith("addx "):
                value = int(line[5:-1])
                register_values.append(register)
                register_values.append(register)
                register += value
        print(sum([i * register_values[i - 1] for i in [20, 60, 100, 140, 180, 220]]))


def part2():
    with open("10_input.txt") as f:
        register = 1
        register_values = []
        for line in f.readlines():
            if line.startswith("noop"):
                register_values.append(register)
            elif line.startswith("addx "):
                value = int(line[5:-1])
                register_values.append(register)
                register_values.append(register)
                register += value

        def get_register_at_cycle(cycle):
            return register_values[min(cycle, len(register_values) - 1)]

        i = 0
        screen = []
        for y in range(0, 240, 40):
            row = ""
            for x in range(40):
                register = get_register_at_cycle(x + y)
                if abs(x - register) <= 1:
                    row += "##"
                else:
                    row += ".."
            screen.append(row)
        print("\n".join(screen))




part1()
part2()