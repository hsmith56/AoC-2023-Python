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

inpt = load()

def part1(data, *args, **kwargs):
    return data

def part2(data, *args, **kwargs):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')