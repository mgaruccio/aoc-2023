## processed in 4minutes 23 seconds on my M1 macbook

from queue import Queue
# FILE_NAME = 'day4/alt.txt'
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


cards= parse_input(input)
unprocessed_cards = cards

card_queue = Queue()
for card in cards:
    card_queue.put(card)

total = len(cards)
while not card_queue.empty():
    current_card = card_queue.get()
    win_count = 0
    for winning_number in current_card['winning_numbers']:
        winner = check_winning_number(winning_number, current_card['numbers_you_have'])
        if winner:
            win_count += 1
    for card in cards[current_card['card_number']:current_card['card_number'] + win_count]:
        card_queue.put(card)
        total += 1
    print(card_queue.qsize())

print('\n')
print(total)



