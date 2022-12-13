import math


class Node:
    def __init__(self, height: int, position: tuple[int, int]):
        self.linked: list[Node] = []
        self.height = height
        self.position = position

    def add_node(self, node: 'Node'):
        self.linked.append(node)

    def __repr__(self):
        return f"<{self.height} -> {','.join([str(x.height) for x in self.linked])}>"


class Graph:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes


def load_map() -> (Graph, Node, Node):
    grid = []
    y = 0
    start_position = end_position = None
    for line in open("12_input.txt"):
        row = []
        grid.append(row)
        x = 0
        for char in line[:-1]:
            if char == "S":
                start_position = (x, y)
                height = 1
            elif char == "E":
                end_position = (x, y)
                height = 26
            else:
                height = ord(char) - ord('a') + 1
            row.append(Node(height, (x, y)))
            x += 1
        y += 1

    if start_position is None or end_position is None:
        return None

    nodes = []
    start_node = end_node = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            node = grid[y][x]
            nodes.append(node)
            if (x, y) == start_position:
                start_node = node
            if (x, y) == end_position:
                end_node = node
            if x > 0:
                x_node = grid[y][x - 1]
                x_difference = node.height - x_node.height
                if x_difference <= 1:
                    x_node.add_node(node)
                if x_difference >= -1:
                    node.add_node(x_node)
            if y > 0 :
                y_node = grid[y - 1][x]
                y_difference = node.height - y_node.height
                if y_difference <= 1:
                    y_node.add_node(node)
                if y_difference >= -1:
                    node.add_node(y_node)

    if start_node is None or end_node is None:
        return None

    return Graph(nodes), start_node, end_node


def find_path(start: Node, end: Node) -> (list[Node], bool):
    to_check = [start]
    searched = set()
    routes = {}

    while len(to_check) > 0:
        node = to_check.pop(0)
        if node == end:
            break
        for neighbour in node.linked:
            if neighbour not in searched and neighbour not in to_check:
                to_check.append(neighbour)
                routes[neighbour] = node
        searched.add(node)
    else:
        return [], False

    distance = 0
    path = []
    while node != start:
        distance += 1
        path.append(str(node.position))
        node = routes[node]
    path.reverse()
    return path, True


def part1():
    heightmap, start, end = load_map()
    path, success = find_path(start, end)
    print(len(path))


def part2():
    heightmap, _, end = load_map()
    starts = []
    for node in heightmap.nodes:
        if node.height == 1:
            starts.append(node)

    minimum = 1_000_000
    for start in starts:
        path, success = find_path(start, end)
        if success:
            minimum = min(minimum, len(path))
    print(minimum)


part1()
part2()
