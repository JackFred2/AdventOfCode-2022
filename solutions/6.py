def part1():
    max_length = 4
    with open("6_input.txt") as f:
        string = f.readline()

    recent = []
    i = 1
    for char in string:
        recent.append(char[0])
        if len(recent) > max_length:
            recent.pop(0)
        if len(set(recent)) == max_length:
            print(i)
            break
        i += 1


def part2():
    max_length = 14
    with open("6_input.txt") as f:
        string = f.readline()

    recent = []
    i = 1
    for char in string:
        recent.append(char[0])
        if len(recent) > max_length:
            recent.pop(0)
        if len(set(recent)) == max_length:
            print(i)
            break
        i += 1


part1()
part2()
