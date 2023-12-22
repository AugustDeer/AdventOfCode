from functools import reduce
import operator as op

def is_zeros(ns: list[int]) -> bool:
    for n in ns:
        if n != 0:
            return False
    return True

def cons_diff(ns: list[int]) -> list[int]:
    return [ns[i+1]-n for i, n in enumerate(ns[:-1])]

def repeated_diffs(ns: list[int]) -> list[list[int]]:
    steps = [ns]
    while not is_zeros(steps[-1]):
        steps.append(cons_diff(steps[-1]))
    return steps

def extrapolate(ns: list[int]) -> int:
    steps = repeated_diffs(ns)
    steps[-1].append(0)
    for i, step in reversed(list(enumerate(steps))[:-1]):
        step.append(step[-1]+steps[i+1][-1])
    return steps[0][-1]

def preapolate(ns: list[int]) -> int:
    steps = repeated_diffs(ns)
    pre_num = 0
    for step in reversed(steps[:-1]):
        pre_num = step[0] - pre_num
    return pre_num

def parse1(nums_str: str) -> int:
    return extrapolate([int(n) for n in nums_str.split()])

def parse2(nums_str: str) -> int:
    return preapolate([int(n) for n in nums_str.split()])

def part(n):
    func = parse1 if n == 1 else parse2
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return reduce(op.add, map(func, input))

print(part(1))
print(part(2))