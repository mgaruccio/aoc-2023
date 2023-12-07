import re

FILE_NAME = "day3/example_input.txt"
FILE_NAME = "day3/input.txt"
# FILE_NAME = "day3/altexample.txt"

not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


def split_string(s):
    return [x for x in s]


matrix = [split_string(x) for x in input]





def get_part_positions(line_number: int, gear_position: int):
    lines_to_search = [line_number]
    if line_number != 0:
        lines_to_search.insert(0, line_number - 1)
    if line_number < len(input):
        lines_to_search.append(line_number + 1)
    start = gear_position - 1 if gear_position != 0 else gear_position
    end = gear_position +1 if gear_position < len(input[line_number]) - 1 else gear_position


    part_positions = []
    for line in lines_to_search:
        for i in range(start, end + 1):
            if matrix[line][i].isnumeric():
                part_positions.append((line, i))

    if len(part_positions) == 1:
        return part_positions
    for idx, part in enumerate(part_positions):
        if part[1] - 1 == part_positions[idx - 1][1] and part[0] == part_positions[idx - 1][0]:
            del part_positions[idx - 1]
    for idx, part in enumerate(part_positions):
        if part[1] - 1 == part_positions[idx - 1][1] and part[0] == part_positions[idx - 1][0]:
            del part_positions[idx - 1]
    return part_positions


def get_part_number_span(line_number: int, position: int):
    line = matrix[line_number]
    start = position
    end = position
    while True:
        if not line[start - 1].isnumeric():
            break
        start -= 1
    while True:
        if end >= len(line) -1:
            break
        if not line[end + 1].isnumeric():
            break
        end += 1
    return (start, end)


def calculate_gear(line_number: int, gear_position: int):
    part_positions = get_part_positions(line_number, gear_position)
    if len(part_positions) != 2:
        return None
    parts = []
    for part in part_positions:
        part_number_span = get_part_number_span(part[0], part[1])
        part_number = "".join(matrix[part[0]][part_number_span[0]:part_number_span[1] + 1])
        parts.append(part_number)
    return int(parts[0]) * int(parts[1])



gear_values = []
for line_number, line in enumerate(input):
    matches = re.finditer("\\*", line)
    for m in matches:
        if m.group() == "":
            continue
        gear_value = calculate_gear(line_number, m.start())
        print(f"{line_number} - {gear_value}")

        if gear_value:
            gear_values.append(gear_value)


print(sum(gear_values))
