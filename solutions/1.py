def part1():
    with open("1_input.txt") as f:
        max_calories = 0
        current_elf_sum = 0
        for line in f.readlines():
            if line == "\n":
                max_calories = max(current_elf_sum, max_calories)
                current_elf_sum = 0
            else:
                current_elf_sum += int(line)

    print(max_calories)


def part2():
    with open("1_input.txt") as f:
        sums = []
        current_elf_sum = 0
        for line in f.readlines():
            if line == "\n":
                sums.append(current_elf_sum)
                current_elf_sum = 0
            else:
                current_elf_sum += int(line)

    sums.sort()

    print(sum(sums[-3:]))


part1()
part2()
