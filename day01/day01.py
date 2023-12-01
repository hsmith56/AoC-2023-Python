import random, math

def load(example=False):
    if example is True:
        with open('day01/day01Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day01/day01Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(example=False)

def part1(data, *args, **kwargs):
    total = 0
    for entry in data:
        nums = [x for x in entry if x.isnumeric()]
        first, last = nums[0], nums[-1]
        total += int(f"{first}{last}")
    
    return total

def part2(data, *args, **kwargs):
    mapping = { "one": 'one1one',
                "two": 'two2two',
                "three":'three3three',
                "four": 'four4four',
                "five": 'five5five',
                "six": 'six6six',
                "seven":'seven7seven',
                "eight":'eight8eight',
                "nine":'nine9nine'
            }

    total = 0
    for entry in data:
        for k,v in mapping.items():
            entry = entry.replace(k, v)
        
        nums = [x for x in entry if x.isnumeric()]
        first, last = nums[0], nums[-1]
        total += int(f"{first}{last}")
    
    return total

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')