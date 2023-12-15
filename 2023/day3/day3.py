from functools import reduce
import operator as op
from collections import defaultdict

def adjacent(x: int, y: int, width: int, height: int) -> list:
    output = []
    for adj_x in range(max(x-1,0),min(x+2,width)):
        for adj_y in range(max(y-1,0),min(y+2,height)):
            if adj_x != x or adj_y != y:
                output.append((adj_x,adj_y))
    return output

def parse(schematic: list) -> list:
    output = []
    current_part = ""
    valid_part = False

    height = len(schematic)
    width = len(schematic[0])

    for y in range(height):
        for x in range(width):
            char = schematic[y][x]
            if char in "0123456789":
                current_part += char
                for adj_x, adj_y in adjacent(x,y,width,height):
                    if schematic[adj_y][adj_x] not in ".0123456789":
                        valid_part = True
            else:
                if valid_part:
                    #print("Valid:", current_part)
                    output.append(int(current_part))
                #elif current_part != "":
                    #print("Invalid:", current_part)
                current_part = ""
                valid_part = False
        if valid_part:
            output.append(int(current_part))
        current_part = ""
        valid_part = False
    return output


def gear_parse(schematic: list) -> list:
    output = []
    gear_dict = defaultdict(int)
    current_part = ""
    current_gear = (0,0)
    valid_part = False

    height = len(schematic)
    width = len(schematic[0])

    for y in range(height):
        for x in range(width):
            char = schematic[y][x]
            if char in "0123456789":
                current_part += char
                for adj_x, adj_y in adjacent(x,y,width,height):
                    if schematic[adj_y][adj_x] == '*':
                        current_gear = (adj_x,adj_y)
                        valid_part = True
            else:
                if valid_part:
                    if gear_dict[current_gear] == 0:
                        gear_dict[current_gear] = int(current_part)
                    else:
                        output.append(gear_dict[current_gear]*int(current_part))
                current_part = ""
                valid_part = False
                current_gear = (0,0)
        if valid_part:
            if gear_dict[current_gear] == 0:
                gear_dict[current_gear] = int(current_part)
            else:
                output.append(gear_dict[current_gear]*int(current_part))
        current_part = ""
        valid_part = False
        current_gear = (0,0)
    return output

def part(n):
    func = parse if n == 1 else gear_parse
    with open("input.txt") as input_file:
        input_str = input_file.read().strip().split('\n')
        return reduce(op.add, func(input_str))

test ="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')

#print(reduce(op.add, parse(test)))

print(part(1))
print(part(2))