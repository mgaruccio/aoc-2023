FILE_NAME = "day1/input.txt"
# FILE_NAME = "day1/example_input_2.txt"

num_strings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]


def find_first_number(s):
    for c in s:
        try:
            int(c)
            return c
        except:
            continue


def convert_num_strings(s):
    for string in num_strings:
        s = convert_all(s, string)
    return s


def convert_all(s, i, start=0):
    l = list(s)
    t = s.find(i, start)
    if t != -1:
        l.insert(t + 1, num_strings[i])
        s = convert_all("".join(l), i, start=t + 2)
    return s


numbers = []
for line in input:
    line = convert_num_strings(line)
    reversed = line[::-1]
    first_number = find_first_number(line)
    last_number = find_first_number(reversed)
    s = f"{first_number}{last_number}"
    n = int(s)
    print(n)
    numbers.append(n)

print(sum(numbers))
