import random, math

def load(example=False):
    if example is True:
        with open('day04/day04Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day04/day04Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(True)

def part1(data, *args, **kwargs):
    result = 0
    for line in data:
        winners, _, actuals = line.partition('|')
        winners = [int(x) for x in winners.split(": ")[1].split(" ") if x]
        actuals = [int(x) for x in actuals.split(" ") if x]
        n_wins = len(set(winners) & set(actuals))
        result += round(2**(n_wins-1))

    return int(result)

def part2(data, *args, **kwargs):
    copies = [1] * len(data)
    for card_index, line in enumerate(data):
        winners, _, actuals = line.partition('|')
        winners = [int(x) for x in winners.split(": ")[1].split(" ") if x]
        actuals = [int(x) for x in actuals.split(" ") if x]
        n_wins = len(set(winners) & set(actuals))
        for x in range(card_index+1, card_index+n_wins+1):
            copies[x] += copies[card_index]

    return sum(copies)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')
