import operator
import re


def get_operation(operation_string):
    match = re.match(r"(old|\d+) ([+*]) (old|\d+)", operation_string)
    first = match.group(1)
    operand = operator.mul if match.group(2) == "*" else operator.add
    second = match.group(3)

    def operation(input):
        return operand(input if first == "old" else int(first), input if second == "old" else int(second))

    return operation


def product(collection):
    value = 1
    for item in collection:
        value *= item
    return value


def get_initial_monkey_state():
    with open("11_input.txt") as f:
        lines = f.readlines()
    monkeys = []
    for i in range(0, len(lines), 7):
        monkeys.append({
            "items": [int(x) for x in lines[i + 1][18:-1].split(", ")],
            "operation": get_operation(lines[i + 2][19:-1]),
            "divisor": int(lines[i + 3][21:-1]),
            "true_destination": int(lines[i + 4][29:-1]),
            "false_destination": int(lines[i + 5][30:-1]),
            "inspections": 0
        })
    return monkeys


def calculate(stress_divisor: int, rounds: int):
    monkeys = get_initial_monkey_state()
    worry_divisor_product = product([monkey["divisor"] for monkey in monkeys])

    for round in range(rounds):
        for monkey in monkeys:
            items = monkey["items"]
            monkey["inspections"] += len(items)
            for _ in range(len(items)):
                items[0] = monkey["operation"](items[0]) // stress_divisor % worry_divisor_product
                destination = monkey["true_destination"] if items[0] % monkey["divisor"] == 0 else monkey[
                    "false_destination"]
                monkeys[destination]["items"].append(items.pop(0))
    monkey_business = [monkey["inspections"] for monkey in monkeys]
    monkey_business.sort()
    print(monkey_business[-1] * monkey_business[-2])


def part1():
    calculate(3, 20)


def part2():
    calculate(1, 10_000)


part1()
part2()
