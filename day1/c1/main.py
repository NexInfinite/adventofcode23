print(sum([int([x for x in line.rstrip() if x.isdigit()][0] + [x for x in line.rstrip() if x.isdigit()][-1]) for line in open("words.txt", "r")]))
