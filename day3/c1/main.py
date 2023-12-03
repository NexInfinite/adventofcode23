import string
schematics = [[x for x in line.rstrip()] for line in open("input.txt", "r")]
symbols = list(string.punctuation)
symbols.remove(".")
x_max = len(schematics[0]) - 1
y_max = len(schematics) - 1

def get_3x3(x, y):
    arr = []
    tets_index = [-1, 0, 1]
    for y_change in tets_index:
        y_i = y + y_change
        for x_change in tets_index:
            x_i = x + x_change
            if (x_i >= 0 and x_i <= x_max) and (y_i >= 0 and y_i <= y_max):
                arr.append(schematics[y_i][x_i])
    return arr

def check_digit(x, y):
    if schematics[y][x].isdigit():
        adjacents = get_3x3(x, y)
        for value in adjacents:
            if value in symbols:
                return get_number(x, y)
    return 0
                
def get_number(x, y):
    total = []
    start = x

    # Go back till not digit
    for i in range(x, 0, -1):
        if not schematics[y][i].isdigit():
            start = i + 1
            break

    # count forward till not digit
    for i in range(start, x_max):
        if schematics[y][i].isdigit():
            total.append(schematics[y][i])
        else:
            return int("".join(total))
    return 0 if total == [] else int("".join(total))

def run():
    total = 0
    for y in range(len(schematics)):
        skip = 0
        for x in range(len(schematics[y])):
            if skip > 0:
                skip -= 1
            else:
                dig = check_digit(x, y)
                if dig > 0:
                    total += dig
                    print(dig, len(str(dig)))
                    skip = len(str(dig))
                
    print(total)

run()
