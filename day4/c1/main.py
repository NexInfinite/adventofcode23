cards = [[[int(x) for x in line.rstrip().split(":")[1].split("|")[0].split(" ") if x != ""], [int(x) for x in line.rstrip().split(":")[1] .split("|")[1].split(" ") if x != ""]] for line in open("test.txt")]

total = 0
for card in cards:
    card_score = 0
    [(card_score := 1 if card_score == 0 else card_score*2) for answer in card[0] if answer in card[1]]
    total += card_score
print(total)