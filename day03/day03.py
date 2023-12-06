import random, math, re

def load(example=False):
    if example is True:
        with open('day03/day03Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day03/day03Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(True)

class number_:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __hash__(self):
        return hash((self.x, self.y, self.value))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.value == other.value


def get_symbols(data):
    symbols = []
    for index in range(0, len(data)):
        for position_index, symbol in enumerate(data[index]):
            if not symbol.isnumeric() and symbol != '.':
                symbols.append((index, position_index))
    return symbols

def part1(data, *args, **kwargs):
    symbol_positions = get_symbols(data)
    numbers = []
    for row_n, row in enumerate(data):
        for number in re.finditer(r'\d+', row):
            x, y = number.start()-1, number.end()+1
            for symbol in symbol_positions:
                if symbol[0] - 1 == row_n or symbol[0] + 1 == row_n or symbol[0] == row_n:
                    if symbol[1] >= x and symbol[1] <= y:
                        numbers.append(number_(x,y, int(number.group())))
    print(len(numbers), len(set(numbers)))                   
    return sum([x.value for x in list(set(numbers))])

def part2(data, *args, **kwargs):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')