from functools import reduce
import operator as op
import math

input = [(49,263),(97,1532),(94,1378),(94,1851)]

def dist(hold: int, time: int) -> int:
    return hold*(time-hold)

def possible(time: int, rec: int) -> int:
    return len([0 for hold in range(time) if dist(hold, time) > rec])

def parse1(tup: tuple):
    return possible(tup[0],tup[1])

input2 = (49979494, 263153213781851)

def fast_possible(time: int, rec: int) -> int:
    # hold*(time-hold) > rec
    # hold^2-hold*time+rec < 0
    # hold in (time +- sqrt(time^2-4*rec))/2
    min_hold = (time - math.sqrt(time**2-4*rec))/2
    max_hold = (time + math.sqrt(time**2-4*rec))/2
    return math.ceil(max_hold-1)-math.floor(min_hold+1)+1


def parse2(tup: tuple):
    return fast_possible(tup[0],tup[1])

def part(n: int):
    if n == 1:
        return reduce(op.mul, map(parse1, input))
    else:
        return parse2(input2)

print(part(1))
print(part(2))