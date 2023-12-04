import string
schematics = [[x for x in line.rstrip()] for line in open("input.txt", "r")]
symbols = list(string.punctuation)
symbols.remove(".")
x_max = len(schematics[0]) - 1
y_max = len(schematics) - 1
                
def get_number(x, y):
    global schematics
    total = []
    start = x

    # Go back till not digit
    for i in range(x, -1, -1):
        if not schematics[y][i].isdigit():
            start = i + 1
            break
        if i == 0:
            start = 0

    print(start)
    # count forward till not digit
    for i in range(start, x_max):
        if schematics[y][i].isdigit():
            total.append(schematics[y][i])
            schematics[y][i] = "."
        else:
            return int("".join(total))
    return 0 if total == [] else int("".join(total))

def gear_scan(x, y):
    numbers = []
    y_diffs = [-1, 0, 1]
    for y_diff in y_diffs:
        if 0 <= y + y_diff <= y_max:
            new_y = y + y_diff
            if schematics[new_y][x].isdigit():
                numbers.append(get_number(x, new_y))
            if x - 1 >= 0 and schematics[new_y][x - 1].isdigit():
                numbers.append(get_number(x - 1, new_y))
            if x + 1 <= x_max and schematics[new_y][x + 1].isdigit():
                numbers.append(get_number(x + 1, new_y))
    print(numbers)
    return sum(numbers)

def run():
    total = 0
    for y in range(len(schematics)):
        for x in range(len(schematics[y])):
            if not schematics[y][x].isdigit() and schematics[y][x] != ".":
                total += gear_scan(x, y)
    print(total)

if __name__ == "__main__":
    # for x in range(len(schematics[1])):
    #     if schematics[1][x] in symbols:
    #         gear_scan(x, 1)
    run()
    # for schema in schematics:
    #     print("".join(schema))