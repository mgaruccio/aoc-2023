FILE_NAME = "day1/input.txt"

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


def find_first_number(s):
    for c in s:
        try:
            int(c)
            return c
        except:
            continue


numbers = []
for line in input:
    reversed = line[::-1]
    first_number = find_first_number(line)
    last_number = find_first_number(reversed)
    s = f"{first_number}{last_number}"
    n = int(s)
    numbers.append(n)

print(sum(numbers))
