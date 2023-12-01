numbers = []
number_mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("words.txt", "r") as f:
    for line in f:
        word = line.rstrip()
        digits = []
        for i in range(len(word)):
            if word[i].isdigit():
                digits.append(word[i])
            else:
                for number in number_mapping:
                    if i + len(number) <= len(word) and word[i:i+len(number)].lower() == number:
                        digits.append(number_mapping[number])
        numbers.append(int(digits[0] + digits[-1]))
print(sum(numbers))