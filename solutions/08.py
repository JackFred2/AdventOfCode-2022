def part1():
    with open("08_input.txt") as f:
        trees = []
        for line in f.readlines():
            row = []
            trees.append(row)
            for tree in line[:-1]:
                row.append(int(tree))

    visible_count = 0
    height = len(trees)
    width = len(trees[0])
    for y in range(len(trees)):
        row = trees[y]
        for x in range(len(row)):
            tree_height = trees[y][x]

            covered_right = False
            for x2 in range(x + 1, width):
                if trees[y][x2] >= tree_height:
                    covered_right = True
                    break

            covered_left = False
            for x2 in range(x - 1, -1, -1):
                if trees[y][x2] >= tree_height:
                    covered_left = True
                    break

            covered_down = False
            for y2 in range(y + 1, height):
                if trees[y2][x] >= tree_height:
                    covered_down = True
                    break

            covered_up = False
            for y2 in range(y - 1, -1, -1):
                if trees[y2][x] >= tree_height:
                    covered_up = True
                    break

            if not covered_up or not covered_down or not covered_left or not covered_right:
                visible_count += 1
    print(visible_count)


def part2():
    with open("08_input.txt") as f:
        trees = []
        for line in f.readlines():
            row = []
            trees.append(row)
            for tree in line[:-1]:
                row.append(int(tree))

    max_score = -1
    height = len(trees)
    width = len(trees[0])
    for y in range(len(trees)):
        row = trees[y]
        for x in range(len(row)):
            score = 1
            tree_height = trees[y][x]

            covered_right = False
            for x2 in range(x + 1, width):
                if trees[y][x2] >= tree_height:
                    covered_right = True
                    score *= abs(x2 - x)
                    break
            if not covered_right:
                score *= (width - x - 1)

            covered_left = False
            for x2 in range(x - 1, -1, -1):
                if trees[y][x2] >= tree_height:
                    covered_left = True
                    score *= abs(x2 - x)
                    break
            if not covered_left:
                score *= x

            covered_down = False
            for y2 in range(y + 1, height):
                if trees[y2][x] >= tree_height:
                    covered_down = True
                    score *= abs(y2 - y)
                    break
            if not covered_down:
                score *= (height - y - 1)

            covered_up = False
            for y2 in range(y - 1, -1, -1):
                if trees[y2][x] >= tree_height:
                    covered_up = True
                    score *= abs(y2 - y)
                    break
            if not covered_up:
                score *= y

            max_score = max(max_score, score)
    print(max_score)


part1()
part2()
