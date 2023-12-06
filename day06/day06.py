import random, math, re
import collections

def load(example=False):
    if example is True:
        with open('day06/day06Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day06/day06Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(False)

def part1(data, *args, **kwargs):
    for index, line in enumerate(data):
        if index == 0:
            hold_times = [int(x.group()) for x in re.finditer(r'\d+', line.split("Time: ")[1])]
        elif index == 1:
            distances = [int(x.group()) for x in re.finditer(r'\d+', line.split("Distance: ")[1])]
    ways_to_win = 1
    for index in range(len(hold_times)):
        to_beat = distances[index]
        ways_to_win *= len([x for x in range(1, hold_times[index]) if (hold_times[index]-x) * x > distances[index]])
    
    return ways_to_win

def part2(data, *args, **kwargs):
    for index, line in enumerate(data):
        if index == 0:
            hold_times = int("".join(line.split("Time: ")[1]).replace(" ",""))
        elif index == 1:
            to_beat = int("".join(line.split("Distance: ")[1]).replace(" ",""))

    losing_hold_times = 0
    for x in range(0, int(hold_times*.25)):
        if (hold_times-x) * x < to_beat:
            losing_hold_times += 1
        else:
            break
    losing_hold_times *= 2
    losing_hold_times -= 1
    ways_to_win = hold_times - losing_hold_times

    return ways_to_win

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')