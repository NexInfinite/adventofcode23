cards = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.rstrip().split(":")[1]
        winning = [int(x) for x in line.split("|")[0].split(" ") if x != ""]
        answers = [int(x) for x in line.split("|")[1].split(" ") if x != ""]
        cards.append([winning, answers])

total = 0
for card in cards:
    card_score = 0
    for answer in card[0]:
        if answer in card[1]:
            card_score = 1 if card_score == 0 else card_score + card_score
    total += card_score
print(total)