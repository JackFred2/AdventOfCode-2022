import copy
import re


# yeah it's just JSON but don't think that's the point
def load():
    data = []
    for line in open("13_input.txt"):
        if line != "\n":
            data.append(parse_list(line[1:-2]))

    return data


def build_stack(stack: list):
    result = []
    while len(stack) > 0:
        ins = stack.pop(0)
        if ins == "[":
            result.append(build_stack(stack))
        elif ins == "]":
            break
        else:
            result.append(ins)
    return result


def parse_list(string: str):
    stack = []
    i = 0
    while i < len(string):
        if string[i].isdigit():
            number = re.match(r"^\d+", string[i:]).group(0)
            stack.append(int(number))
            i += len(number) - 1
        elif string[i] == "[":
            stack.append("[")
        elif string[i] == "]":
            stack.append("]")
        i += 1

    built = build_stack(stack)
    return built


def compare(left: list, right: list) -> bool | None:
    while True:
        if len(left) == 0:
            if len(right) == 0:
                return None
            else:
                return True
        if len(right) == 0:
            return False

        left_item = left.pop(0)
        right_item = right.pop(0)
        if type(left_item) == list or type(right_item) == list:
            if type(left_item) != list:
                left_item = [left_item]
            if type(right_item) != list:
                right_item = [right_item]
            sub_compare = compare(left_item, right_item)
            if sub_compare is not None:
                return sub_compare
        else:
            if left_item < right_item:
                return True
            elif right_item < left_item:
                return False


def part1():
    data = load()
    pairs = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    sum = 0
    for i, (left, right) in zip(range(1, len(pairs) + 1), pairs):
        result = compare(left, right)
        if result:
            sum += i
    print(sum)


def part2():
    data = load()
    divider_a = [[2]]
    divider_b = [[6]]
    data.append(divider_a)
    data.append(divider_b)
    not_sorted = True
    while not_sorted:  # bubble sort
        not_sorted = False
        for i in range(len(data) - 1):
            comparison = compare(copy.deepcopy(data[i]), copy.deepcopy(data[i + 1]))
            if not comparison:
                data[i], data[i + 1] = data[i + 1], data[i]
                not_sorted = True
    print((data.index(divider_a) + 1) * (data.index(divider_b) + 1))


part1()
part2()
