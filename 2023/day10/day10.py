from copy import copy
from enum import Enum
from dataclasses import dataclass
import functools
import math

@dataclass
class Point:
    x: float
    y: float


class Pipe(Enum):
    VERTICAL    = "|"
    HORIZONTAL  = "-"
    NORTH_EAST  = "L"
    NORTH_WEST  = "J"
    SOUTH_WEST  = "7"
    SOUTH_EAST  = "F"
    GROUND      = "."
    START       = "S"

class PipeField:
    start_type: Pipe = Pipe.VERTICAL # You could probably figure this out programatically but I'm lazy

    def __init__(self, pipe_strs: list[str]):
        self.pipes: list[list[Pipe]]
        self.start_pos: Point
        self.pipes, self.start_pos = PipeField.parse(pipe_strs)
        self.pos: Point = copy(self.start_pos)
        self.prev_pos: Point = copy(self.pos)
    
    @staticmethod
    def parse(pipe_strs: list[str]) -> tuple[list[list[Pipe]], Point]:
        pipes = []
        start_pos: Point
        for y, pipe_str in enumerate(pipe_strs):
            if 'S' in pipe_str:
                start_pos = Point(pipe_str.index('S'), y)
            pipes.append([Pipe(p) for p in pipe_str])
        return pipes, start_pos
    
    @functools.cached_property
    def loop(self) -> list[Point]:
        out = [self.prev_pos]
        while True:
            self.move()
            out.append(self.prev_pos)
            if self.pos == self.start_pos:
                break
        return out

    def move(self):
        match self.pipes[self.pos.y][self.pos.x]:
            case Pipe.VERTICAL | Pipe.START:
                if self.pos.y == self.prev_pos.y + 1:
                    self.prev_pos = copy(self.pos)
                    self.pos.y += 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.y -= 1
            case Pipe.HORIZONTAL:
                if self.pos.x == self.prev_pos.x + 1:
                    self.prev_pos = copy(self.pos)
                    self.pos.x += 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.x -= 1
            case Pipe.NORTH_EAST:
                if self.pos.x == self.prev_pos.x:
                    self.prev_pos = copy(self.pos)
                    self.pos.x += 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.y -= 1
            case Pipe.NORTH_WEST:
                if self.pos.x == self.prev_pos.x:
                    self.prev_pos = copy(self.pos)
                    self.pos.x -= 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.y -= 1
            case Pipe.SOUTH_EAST:
                if self.pos.x == self.prev_pos.x:
                    self.prev_pos = copy(self.pos)
                    self.pos.x += 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.y += 1
            case Pipe.SOUTH_WEST:
                if self.pos.x == self.prev_pos.x:
                    self.prev_pos = copy(self.pos)
                    self.pos.x -= 1
                else:
                    self.prev_pos = copy(self.pos)
                    self.pos.y += 1

def parse1(input):
    pipe_field = PipeField(input)
    loop = pipe_field.loop
    return math.floor(len(loop)/2)

def parse2(input):
    pass

def part(n):
    func = parse1 if n == 1 else parse2
    with open("input.txt") as input_file:
        input = input_file.read().strip().split('\n')
        return func(input)
    
print(part(1))