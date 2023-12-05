# cards = [[[int(x) for x in line.rstrip().split(":")[1].split("|")[0].split(" ") if x != ""], [int(x) for x in line.rstrip().split(":")[1].split("|")[1].split(" ") if x != ""]] for line in open("test.txt")]
cards = [[[int(x) for x in line.rstrip().split(":")[1].split("|")[0].split(" ") if x != ""], [int(x) for x in line.rstrip().split(":")[1].split("|")[1].split(" ") if x != ""]] for line in open("input.txt")]

card_scores = {}
curr_card = 0
for card in cards:
    if curr_card not in card_scores:
        card_scores[curr_card] = 1
    else:
        card_scores[curr_card] += 1

    card_score = 0
    for answer in card[0]:
        if answer in card[1]:
            card_score += 1

    for copy_card in range(curr_card + 1, min(curr_card + card_score + 1, len(cards))):
        if copy_card in card_scores:
            card_scores[copy_card] += card_scores[curr_card]
        else:
            card_scores[copy_card] = card_scores[curr_card]

    print(curr_card, card_score, card_scores)
    curr_card += 1

print(sum(card_scores.values()))
    