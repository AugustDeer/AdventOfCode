from functools import reduce
import operator as op
import re

def clean_line1(line):
    digits = list(filter(lambda c: c.isdigit(), line))
    return int(digits[0]+digits[-1])

def clean_line2(line):
    valid_digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    valid = re.findall(r"[0-9]|zero|one|two|three|four|five|six|seven|eight|nine",line)
    digits = list(map(lambda d: d if d.isdigit() else str(valid_digits.index(d)), valid))
    return int(digits[0]+digits[-1])

def part(n):
    clean_line = clean_line1 if n == 1 else clean_line2
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return reduce(op.add, map(clean_line, input))

print(part(1))
print(part(2))