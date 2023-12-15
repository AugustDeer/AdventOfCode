from functools import reduce
import operator as op

def parse(card: str) -> tuple:
    id_str, card_str = card.split(": ")
    _, id_str = id_str.split()
    id = int(id_str)

    winning_str, nums_str = card_str.split(" | ")
    winning = list(map(int, winning_str.split()))
    nums = list(map(int, nums_str.split()))

    return id, winning, nums

def matches(card: str) -> int:
    _, winning, nums = parse(card)
    pts = 0
    for n in winning:
        if n in nums:
            pts += 1
    return pts

def points(cards: list) -> list:
    ms = map(matches, cards)
    return list(map(lambda m: 0 if m == 0 else 2**(m-1), ms))




def total_cards(cards: list) -> list:
    n = len(cards)
    count = [1]*n
    for i in range(n):
        m = matches(cards[i])
        for j in range(m):
            if i+j+1<n:
                count[i+j+1] += count[i]
    return count


def part(n):
    func = points if n == 1 else total_cards
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return reduce(op.add, func(input))

test = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

#print(reduce(op.add, map(points, test)))

print(part(1))
print(part(2))