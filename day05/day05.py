import random, math
from collections import OrderedDict

def load(example=False):
    if example is True:
        with open('day05/day05Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day05/day05Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(True)


def part1(data, *args, **kwargs):
    seeds = []
    all_seeds = []
    mappings = OrderedDict()
    map_index = 0
    for line in data:
        if "seeds:" in line:
            seeds = [int(x) for x in line.split("seeds: ")[1].strip().split(" ")]

    for seed in seeds:
        map_ranges = []
        for line in data:
            if "seeds:" in line:
                continue
            if line:
                if "-" in line:
                    if len(map_ranges) >= 1:
                        for r in map_ranges:
                            if seed in r[0]:
                                seed = seed + r[1]
                                break
                            
                    map_ranges = []
                else:
                    line = [int(x) for x in line.split(" ")]
                    destination, source, increment = line
                    map_ranges.append((range(source, source + increment), destination-source))

        all_seeds.append(seed)

    return min(all_seeds)

def part2(data, *args, **kwargs):
    data.reverse()
    seeds = []
    seed_ranges = []
    all_seeds = []
    mappings = OrderedDict()
    map_index = 0
    for line in data:
        print(line)
        if "seeds:" in line:
            seeds = [int(x) for x in line.split("seeds: ")[1].strip().split(" ")]
            for i in range(0, len(seeds)-1, 2):
                seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))
    for r in seed_ranges:
        for seed in r:
            map_ranges = []
            for line in data:
                if "seeds:" in line:
                    continue
                if line:
                    if "-" in line:
                        if len(map_ranges) >= 1:
                            for r in map_ranges:
                                if seed >= r[0][0] and seed <= r[0][1]:
                                    seed = seed + r[1]
                                    break
                                
                        map_ranges = []
                    else:
                        line = [int(x) for x in line.split(" ")]
                        destination, source, increment = line
                        if seed < destination and seed < source:
                            continue
                        map_ranges.append(((source, source + increment), destination-source))
            
            all_seeds.append(seed)

    return min(all_seeds)

def part2_(data, *args, **kwargs):
    seed_ranges = []
    all_seeds = []
    mappings = OrderedDict()
    map_index = 0
    largest_start = 0
    for line in data:
        if "seeds:" in line:
            seeds = [int(x) for x in line.split("seeds: ")[1].strip().split(" ")]
            for i in range(0, len(seeds)-1, 2):
                largest_start = max(largest_start, seeds[i] + seeds[i+1])



    for seeds in seed_ranges:
        for seed in seeds:
            map_ranges = []
            for line in data:
                if "seeds:" in line:
                    continue
                if line:
                    if "-" in line:
                        if len(map_ranges) >= 1:
                            for r in map_ranges:
                                if seed in r[0]:
                                    seed = seed + r[1]
                                    break
                                
                        map_ranges = []
                    else:
                        line = [int(x) for x in line.split(" ")]
                        destination, source, increment = line
                        map_ranges.append((range(source, source + increment), destination-source))

            all_seeds.append(seed)

    return min(all_seeds)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')

