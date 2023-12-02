import random, math

def load(example=False):
    if example is True:
        with open('day02/day02Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day02/day02Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(False)

def part1(data, *args, **kwargs):
    # 🤮 
    rules = {"red": 12, "green": 13, "blue": 14}
    invalid_games = []
    for game_number, line in enumerate(data):
        line = line.split(':')[1]
        draws = [x.strip() for x in line.split(';')]
        for draw in draws:
            drawings = {b: int(a) for a,b in [str(k).split(' ') for k in [x for x in draw.split(', ')]]}
            for k, v in drawings.items():
                if rules[k] < v:
                    invalid_games.append(game_number+1)
                    break

    return sum(range(1, len(data)+1)) - sum(list(set(invalid_games)))

def part2(data, *args, **kwargs):
    rules = {"red": 12, "green": 13, "blue": 14}
    powers = []
    for game_number, line in enumerate(data):
        line = line.split(':')[1]
        draws = [x.strip() for x in line.split(';')]
        collection = []
        for draw in draws:
            drawings = {b: int(a) for a,b in [str(k).split(' ') for k in [x for x in draw.split(', ')]]}
            collection.append(drawings)
        red_max, blue_max, green_max = 0,0,0
        for pull in collection:
            for k,v in pull.items():
                if k == 'blue':
                    blue_max = max(blue_max, v)
                elif k == 'red':
                    red_max = max(red_max, v)
                elif k == 'green':
                    green_max = max(green_max, v) 
        powers.append(blue_max * green_max * red_max)
    return sum(powers)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')