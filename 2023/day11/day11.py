from copy import copy
from functools import reduce
import operator as op
import numpy as np
import einops
import bisect

def expand(universe: np.ndarray) -> np.ndarray:
    expanded = universe
    i = 0
    while i < expanded.shape[0]:
        if np.all(expanded[i,:] == '.'):
            expanded = np.insert(expanded, i+1, expanded[i,:], axis=0)
            i += 1
        i += 1
    i = 0
    while i < expanded.shape[1]:
        if np.all(expanded[:,i] == '.'):
            expanded = np.insert(expanded, i+1, expanded[:,i], axis=1)
            i += 1
        i += 1
    return expanded

def galaxies(universe: np.ndarray) -> np.ndarray:
    out = []
    for pos, char in np.ndenumerate(universe):
        if char == '#':
            out.append(pos)
    return np.array(out)

def distances(points: np.ndarray):
    diff = np.abs(points[:, None] - points)
    dist = einops.reduce(diff, 'a b c -> a b', 'sum')
    return einops.rearrange(np.tril(dist, 0), 'a b -> (a b)')

def parse1(universe):
    expanded = expand(universe)
    gal = galaxies(expanded)
    return distances(gal)



def empty_rows(universe: np.ndarray) -> tuple[list, list]:
    rows = []
    cols = []
    for i in range(universe.shape[0]):
        if np.all(universe[i,:] == '.'):
            rows.append(i)
    for i in range(universe.shape[1]):
        if np.all(universe[:,i] == '.'):
            cols.append(i)
    return rows, cols

EXPAND_SCALE = 1000000

def expand2(gals: np.ndarray, empty: tuple[list]):
    out = []
    e_rows, e_cols = empty
    for g in gals:
        rows = bisect.bisect(e_rows, g[0])
        cols = bisect.bisect(e_cols, g[1])
        out.append([g[0]+rows*(EXPAND_SCALE-1), g[1]+cols*(EXPAND_SCALE-1)])
    return np.array(out, dtype=np.int64)

def parse2(universe):
    gals = galaxies(universe)
    empty = empty_rows(universe)
    expand_gals = expand2(gals, empty)
    return distances(expand_gals)

def part(n):
    func = parse1 if n == 1 else parse2
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        universe = np.array([list(r) for r in input])
        return reduce(op.add, func(universe))

test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

test2 = """#.#.#"""

#print(reduce(op.add, parse2(np.array([list(r) for r in test.split('\n')]))))
print(part(1))
print(part(2))