import re


def part1():
    with open("07_input.txt") as f:
        pwd = []
        files = {}

        def get_current():
            current_dir = files
            for path_segment in pwd:
                current_dir = current_dir[path_segment]
            return current_dir

        for line in f.readlines():
            line = line[:-1]
            if line.startswith("$ cd "):
                reading_ls = False
                path = line[5:]
                if path == "..":
                    pwd.pop()
                elif path == "/":
                    pwd = []
                else:
                    pwd.append(path)
            elif line.startswith("$ ls"):
                reading_ls = True
            elif reading_ls:
                current = get_current()
                if line.startswith("dir"):
                    current[line[4:]] = {}
                else:
                    match = re.match("(\d+) (.+)", line)
                    size = match.group(1)
                    name = match.group(2)
                    current[name] = int(size)

        below_threshold_list = []

        def populate_size(file_list, tally_list: list[int]):
            total = 0
            for (key, value) in file_list.items():
                if type(value) == int:
                    total += value
                else:
                    total += populate_size(value, tally_list)
            file_list["_size"] = total
            if total <= 100_000:
                below_threshold_list.append(total)
            return total

        populate_size(files, below_threshold_list)

        print(sum(below_threshold_list))


def part2():
    with open("07_input.txt") as f:
        pwd = []
        files = {}

        def get_current():
            current_dir = files
            for path_segment in pwd:
                current_dir = current_dir[path_segment]
            return current_dir

        for line in f.readlines():
            line = line[:-1]
            if line.startswith("$ cd "):
                reading_ls = False
                path = line[5:]
                if path == "..":
                    pwd.pop()
                elif path == "/":
                    pwd = []
                else:
                    pwd.append(path)
            elif line.startswith("$ ls"):
                reading_ls = True
            elif reading_ls:
                current = get_current()
                if line.startswith("dir"):
                    current[line[4:]] = {}
                else:
                    match = re.match("(\d+) (.+)", line)
                    size = match.group(1)
                    name = match.group(2)
                    current[name] = int(size)

        dir_size_list = []

        def populate_size(file_list, tally_list: list[int]):
            total = 0
            for (key, value) in file_list.items():
                if type(value) == int:
                    total += value
                else:
                    total += populate_size(value, tally_list)
            file_list["_size"] = total
            dir_size_list.append(total)
            return total

        populate_size(files, dir_size_list)

        dir_size_list.sort()

        needed_space = 30_000_000
        max_space = 70_000_000
        free_space = max_space - files["_size"]
        needed_to_clear = needed_space - free_space
        for item in dir_size_list:
            if item > needed_to_clear:
                print(item)
                break


part1()
part2()
