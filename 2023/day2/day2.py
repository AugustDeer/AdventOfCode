from functools import reduce
import operator as op

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def possible_draw(d: str) -> bool:
    amt, color = d.split()
    if color == "red":
        return int(amt) <= MAX_RED
    if color == "green":
        return int(amt) <= MAX_GREEN
    if color == "blue":
        return int(amt) <= MAX_BLUE

def possible_round(r: str) -> bool:
    draws = r.split(",")
    for d in draws:
        if not possible_draw(d):
            return False
    return True

def possible_game(game: str) -> bool:
    rounds = game.split(";")
    for r in rounds:
        if not possible_round(r):
            return False
    return True

def parse_line(line: str) -> int:
    game_numb, game_str = line.split(": ")
    _, id_str = game_numb.split()
    if possible_game(game_str):
        return int(id_str)
    else:
        return 0


def round_to_array(r: str):
    output = [0,0,0]
    draws = r.split(", ")
    for draw in draws:
        amt, color = draw.split()
        if color == "red":
            output[0] = int(amt)
        elif color == "green":
            output[1] = int(amt)
        elif color == "blue":
            output[2] = int(amt)
    return output

def power(line: str) -> int:
    _, game = line.split(": ")
    rounds = map(round_to_array, game.split("; "))
    output = [0,0,0]
    for r in rounds:
        for i, amt in enumerate(r):
            if output[i] < amt:
                output[i] = amt
    return output[0]*output[1]*output[2]
    


def part(n: int) -> int:
    func = parse_line if n == 1 else power
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return reduce(op.add, map(func, input))

print(part(1))
print(part(2))