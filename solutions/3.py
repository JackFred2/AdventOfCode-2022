def get_priority(char: chr):
    if char.isupper():
        return ord(char) + 1 - ord('A') + 26
    else:
        return ord(char) + 1 - ord('a')


def part1():
    total = 0

    with open("3_input.txt") as f:
        for line in f.readlines():
            first = set(line[:len(line)//2])
            second = set(line[len(line)//2:])

            common = first.intersection(second).pop()
            #print(f"{common}: {get_priority(common)}")
            total += get_priority(common)
    print(total)

def part2():
    total = 0

    with open("3_input.txt") as f:
        lines = f.readlines()
        f.seek(0)
        for _ in range(len(lines)//3):
            item_set = set(f.readline())
            item_set = item_set.intersection(set(f.readline()))
            item_set = item_set.intersection(set(f.readline()))
            item_set.remove('\n')
            total += get_priority(item_set.pop())
    print(total)


part1()
part2()
