from functools import reduce
import operator as op
from collections import defaultdict

class funcdict(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)
    
class SeedRange:
    def __init__(self, ranges: list[tuple[int,int,int]]) -> None:
        self.ranges = ranges
    
    def apply(self, input: int) -> int:
        for r in self.ranges:
            if input >= r[1] and input < r[1]+r[2]:
                return r[0]+input-r[1]
        return input

def parse_chunk(map_str: str) -> SeedRange:
    split_map_str = map_str.split('\n')
    return SeedRange(list(map(lambda m: tuple(map(int, m.split())), split_map_str[1:])))

def apply_maps(start: int, maps: list[SeedRange]) -> int:
    output = start
    for m in maps:
        new = m.apply(output)
        #print(output, new)
        output = new
    return output

def parse(seed_map_str: str) -> tuple:
    split_map_str = seed_map_str.split('\n\n')
    seed_str = split_map_str[0]
    map_strs = split_map_str[1:]

    _, start_seed_str = seed_str.split(": ")
    #print(start_seed_str)
    start_seeds = map(int, start_seed_str.split())

    maps = list(map(parse_chunk, map_strs))

    return start_seeds, maps

def seed_to_loc(seed_str):
    start_seeds, maps = parse(seed_str)
    return list(map(lambda s: apply_maps(s, maps), start_seeds))


def seed_to_loc_2(seed_str):
    start_seeds, maps = parse(seed_str)
    return list(map(lambda s: apply_maps(s, maps), start_seeds))

def part(n):
    func = seed_to_loc
    with open("input.txt") as input_file:
        input = input_file.read().strip()
        return min(func(input))
    

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

#print(seed_to_loc(test))

print(part(1))