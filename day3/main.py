import re

FILE_NAME = "day3/example_input.txt"
FILE_NAME = "day3/input.txt"

not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


def split_string(s):
    return [x for x in s]


matrix = [split_string(x) for x in input]


def symbol_search(line_number: int, span: tuple):
    lines_to_search = [line_number]
    if line_number > 0:
        lines_to_search.append(line_number - 1)
    if line_number < len(input) - 1:
        lines_to_search.append(line_number + 1)
    if span[0] != 0:
        span = (span[0] - 1, span[1])
    if span[1] != len(input[line_number]):
        span = (span[0], span[1] + 1)

    for line in lines_to_search:
        for position in range(span[0], span[1]):
            if matrix[line][position] not in not_symbols:
                return True
    return False


part_numbers = []
for line_number, line in enumerate(input):
    matches = re.finditer("\d*", line)
    if line_number == 139:
        print("foo")
    for m in matches:
        if m.group() == "":
            continue
        is_part_number = symbol_search(line_number, m.span())
        print(f"{m.group()} - {is_part_number}")
        if is_part_number:
            part_numbers.append(int(m.group()))

print(sum(part_numbers))
