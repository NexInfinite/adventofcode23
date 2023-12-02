def test_game(game_split):
    min_cubes = {"red": 1, "green": 1, "blue": 1}
    for game in game_split:
        for cube in game.split(","):
            cube_num = int(cube.split(" ")[1])
            cube_colour = cube.split(" ")[2]
            min_cubes[cube_colour] = cube_num if cube_num > min_cubes[cube_colour] else min_cubes[cube_colour]
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

total = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        game_info_split = line.split(":")
        game_split = game_info_split[1].split(";")
        total += test_game(game_split)
print(total)