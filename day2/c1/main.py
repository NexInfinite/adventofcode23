def test_game(game_split):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    for game in game_split:
        for cube in game.split(","):
            if int(cube.split(" ")[1]) > max_cubes[cube.split(" ")[2]]:
                return False
    return True

total = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        game_info_split = line.split(":")
        game_id = int(game_info_split[0].split(" ")[1])
        game_split = game_info_split[1].split(";")
        if test_game(game_split):
            total += game_id
print(total)