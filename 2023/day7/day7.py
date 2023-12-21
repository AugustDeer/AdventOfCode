from functools import reduce
import operator as op

import functools
from enum import Enum
from collections import defaultdict

class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Rank(OrderedEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 3
    FULL_HOUSE = 4
    FOUR_KIND = 5
    FIVE_KIND = 6


@functools.total_ordering
class Hand:
    deck = "23456789TJQKA"

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
    
    @functools.cached_property
    def card_count(self) -> dict:
        out = defaultdict(int)
        for card in self.cards:
            out[card] += 1
        return out
    
    @functools.cached_property
    def rank(self) -> Rank:
        values = list(self.card_count.values())
        if 5 in values:
            return Rank.FIVE_KIND
        if 4 in values:
            return Rank.FOUR_KIND
        if 3 in values:
            if 2 in values:
                return Rank.FULL_HOUSE
            return Rank.THREE_KIND
        if 2 in values:
            if values.count(2) == 2:
                return Rank.TWO_PAIR
            return Rank.ONE_PAIR
        return Rank.HIGH_CARD
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return self.cards == other.cards
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        if self.rank < other.rank:
            return True
        if self.rank == other.rank:
            for i in range(5):
                if Hand.deck.find(self.cards[i]) < Hand.deck.find(other.cards[i]):
                    return True
                if Hand.deck.find(self.cards[i]) > Hand.deck.find(other.cards[i]):
                    return False
        return False
    
    def __repr__(self) -> str:
        return f"Hand: {self.cards} Bid: {self.bid}"

def parse1(hand_strs: list[str]) -> int:
    hands = []
    for hand_str in hand_strs:
        card_str, bid_str = hand_str.split()
        hands.append(Hand(card_str, int(bid_str)))
    sorted_hands = sorted(hands)
    return [(i+1)*hand.bid for i, hand in enumerate(sorted_hands)]

@functools.total_ordering
class Hand2:
    deck = "J23456789TQKA"

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
    
    @functools.cached_property
    def card_count(self) -> dict:
        out = defaultdict(int)
        for card in self.cards:
            out[card] += 1
        return out
    
    @functools.cached_property
    def rank(self) -> Rank:
        values = list(self.card_count.values())
        jokers = self.card_count['J']
        joker = jokers > 0
        if 5 in values:
            return Rank.FIVE_KIND
        if 4 in values:
            if joker:
                return Rank.FIVE_KIND
            return Rank.FOUR_KIND
        if 3 in values:
            if 2 in values:
                if joker:
                    return Rank.FIVE_KIND
                return Rank.FULL_HOUSE
            if joker:
                return Rank.FOUR_KIND
            return Rank.THREE_KIND
        if 2 in values:
            if values.count(2) == 2:
                if jokers == 2:
                    return Rank.FOUR_KIND
                if joker:
                    return Rank.FULL_HOUSE
                return Rank.TWO_PAIR
            if joker:
                return Rank.THREE_KIND
            return Rank.ONE_PAIR
        if joker:
            return Rank.ONE_PAIR
        return Rank.HIGH_CARD
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Hand2):
            return NotImplemented
        return self.cards == other.cards
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Hand2):
            return NotImplemented
        if self.rank < other.rank:
            return True
        if self.rank == other.rank:
            for i in range(5):
                if Hand2.deck.find(self.cards[i]) < Hand2.deck.find(other.cards[i]):
                    return True
                if Hand2.deck.find(self.cards[i]) > Hand2.deck.find(other.cards[i]):
                    return False
        return False
    
    def __repr__(self) -> str:
        return f"Hand: {self.cards} Bid: {self.bid}"

def parse2(hand_strs: list[str]) -> int:
    hands = []
    for hand_str in hand_strs:
        card_str, bid_str = hand_str.split()
        hands.append(Hand2(card_str, int(bid_str)))
    sorted_hands = sorted(hands)
    return [(i+1)*hand.bid for i, hand in enumerate(sorted_hands)]

def part(n):
    func = parse1 if n == 1 else parse2
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return reduce(op.add, func(input))

test = ["32T3K 765","T55J5 684","KK677 28","KTJJT 220","QQQJA 483"]

#print(parse1(test))
#print(reduce(op.add, parse1(test)))
print(reduce(op.add, parse2(test)))
print(part(1))
print(part(2))