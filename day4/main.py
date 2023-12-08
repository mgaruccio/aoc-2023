FILE_NAME = "day4/input.txt"
# FILE_NAME = "day4/example_input.txt"

with open(FILE_NAME) as f:
    input = [x.rstrip("\n") for x in f.readlines()]




def parse_input(input):
    parsed_input = []
    for line in input:
        first = line.split(':')
        card_number = int([x for x in first[0].split(' ') if x != ''][1])
        winning_numbers = [int(x) for x in first[1].split('|')[0].strip(' ').split(' ') if x != '']
        numbers_you_have = [int(x) for x in first[1].split('|')[1].strip(' ').split(' ') if x != '']
        parsed_input.append({
            "card_number": card_number,
            "winning_numbers": winning_numbers,
            "numbers_you_have": numbers_you_have
        })
    return parsed_input

def check_winning_number(winning_number, numbers):
    if winning_number in numbers:
        return True
    else:
        return False

def get_card_total(winning_numbers, numbers_you_have):
    winners = 0
    for winning_number in winning_numbers:
        if check_winning_number(winning_number, numbers_you_have):
            winners += 1
    if winners == 1:
        return 1
    if winners == 0:
        return 0
    winners -= 1
    return 2 ** winners

parsed_input = parse_input(input)

total_points = 0
for card in parsed_input:
    card_points = get_card_total(card['winning_numbers'], card['numbers_you_have'])
    print(card_points)
    total_points += card_points

print(total_points)
