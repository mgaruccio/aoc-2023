from math import prod

FILE_NAME = "day2/input.txt"
# FILE_NAME = "day2/example_input_2.txt"

colors = ["red", "blue", "green"]

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


def get_game_results(input):
    game_portion = input.split(":")[1]
    return game_portion.split(";")


def get_counts(round):
    results = [x.lstrip() for x in round.split(",")]
    return {x.split(" ")[1]: int(x.split(" ")[0]) for x in results}


def get_highest_count(game_results):
    highest_results = {"red": 0, "green": 0, "blue": 0}
    for result in game_results:
        counts = get_counts(result)
        for r in highest_results:
            color_count = counts.get(r, 0)
            if color_count > highest_results[r]:
                highest_results[r] = color_count
    return prod(highest_results.values())


game_powers = []
for game in input:
    game_results = get_game_results(game)
    highest_count = get_highest_count(game_results)
    game_powers.append(highest_count)
print(sum(game_powers))
