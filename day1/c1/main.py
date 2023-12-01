numbers = []

with open("words.txt", "r") as f:
    for line in f:
        digits = [x for x in line.rstrip() if x.isdigit()]
        numbers.append(int(digits[0] + digits[-1]))

total = sum(numbers)
print(total)
