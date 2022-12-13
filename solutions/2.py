letters_to_move = {
    'A': 0,
    'X': 0,
    'B': 1,
    'Y': 1,
    'C': 2,
    'Z': 2,
}

letters_to_result = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}

move_to_score = {
    0: 1,
    1: 2,
    2: 3,
}

# result_table[their_move][our_move]
result_table = [
    ['D', 'W', 'L'],
    ['L', 'D', 'W'],
    ['W', 'L', 'D'],
]

result_to_score = {
    'L': 0,
    'D': 3,
    'W': 6,
}


def part1():
    total_score = 0
    with open("2_input.txt") as f:
        for line in f.readlines():
            their_move = letters_to_move[line[0]]
            our_move = letters_to_move[line[2]]

            result = result_table[their_move][our_move]

            total_score += move_to_score[our_move]
            total_score += result_to_score[result]

    print(total_score)


def part2():
    total_score = 0
    with open("2_input.txt") as f:
        for line in f.readlines():
            their_move = letters_to_move[line[0]]
            result = letters_to_result[line[2]]

            our_move = result_table[their_move].index(result)

            total_score += move_to_score[our_move]
            total_score += result_to_score[result]

    print(total_score)


part1()
part2()
