class Tree:
    def __init__(self, node_str: str):
        self.node_dict: dict = self._parse(node_str)
        self.pos = 'AAA'
    
    def _parse(self, node_str: str) -> dict:
        node_dict = dict()
        for line in node_str.split('\n'):
            name = line[0:3]
            left = line[7:10]
            right = line[12:15]
            node_dict[name] = (left,right)
        return node_dict
    
    def left(self):
        self.pos = self.node_dict[self.pos][0]

    def right(self):
        self.pos = self.node_dict[self.pos][1]
    
    def traverse(self, dirs: str):
        i = 0
        while True:
            for dir in dirs:
                i += 1
                if dir == 'L':
                    self.left()
                if dir == 'R':
                    self.right()
                if self.pos == 'ZZZ':
                    return i

class SimulTree:
    def __init__(self, node_str: str):
        self.node_dict, self.pos = self._parse(node_str)
        print(self.pos)
        self.seen_pos = []
    
    def _parse(self, node_str: str) -> tuple[dict, list[str]]:
        node_dict = dict()
        pos = []
        for line in node_str.split('\n'):
            name = line[0:3]
            left = line[7:10]
            right = line[12:15]
            node_dict[name] = (left,right)
            if name[2] == 'A':
                pos.append(name)
        return node_dict, pos
    
    def left(self) -> None:
        for i, pos in enumerate(self.pos):
            self.pos[i] = self.node_dict[pos][0]

    def right(self) -> None:
        for i, pos in enumerate(self.pos):
            self.pos[i] = self.node_dict[pos][1]
    
    def is_end(self) -> bool:
        for pos in self.pos:
            if pos[-1] == 'Z':
                break
        for pos in self.pos:
            if pos[-1] != 'Z':
                return False
        return True

    def traverse(self, dirs: str):
        i = 0
        while True:
            for dir in dirs:
                i += 1
                if dir == 'L':
                    self.left()
                if dir == 'R':
                    self.right()
                if self.is_end():
                    return i

def parse1(input_str: str):
    dirs, node_str = input_str.split('\n\n')
    tree = Tree(node_str)
    return tree.traverse(dirs)

def parse2(input_str: str):
    dirs, node_str = input_str.split('\n\n')
    tree = SimulTree(node_str)
    return tree.traverse(dirs)

def part(n):
    func = parse1 if n == 1 else parse2
    with open("./2023/day8/input.txt") as input_file:
        input = input_file.read().strip()
        return func(input)

print(part(1))
print(part(2))