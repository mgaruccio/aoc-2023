FILE_NAME = "day2/input.txt"
# FILE_NAME = "day2/example_input.txt"

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


MAX_CUBE_COUNTS = {"red": 12, "green": 13, "blue": 14}


def get_game_id(input):
    id_portion = input.split(":")[0]
    return id_portion.split(" ")[1]


def get_game_results(input):
    game_portion = input.split(":")[1]
    return game_portion.split(";")


def validate_game_values(game_results):
    for result in game_results:
        color_results = result.split(",")
        for color_result in color_results:
            count = int(color_result.lstrip().split(" ")[0])
            color = color_result.lstrip().split(" ")[1]
            if count > MAX_CUBE_COUNTS[color]:
                return False
    return True


valid_games = []
for game in input:
    game_id = get_game_id(game)
    game_results = get_game_results(game)
    valid_game = validate_game_values(game_results)
    if valid_game:
        valid_games.append(int(game_id))
    else:
        print(game)
        print("")
print(sum(valid_games))
