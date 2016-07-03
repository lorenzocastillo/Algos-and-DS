from collections import namedtuple
Point = namedtuple("Point", "r c")

class Ant:
    def __init__(self):
        self.pos = Point(0,0)
        self.orientation = 'R'

    def turn(self, in_white):
        rotations_clockwise = ['R','D','L','U']
        index = rotations_clockwise.index(self.orientation)
        if in_white:
            self.orientation = rotations_clockwise[(index + 1) % 4]
        else:
            self.orientation = rotations_clockwise[(index - 1 + 4) % 4]

    def move(self):
        r, c = self.pos
        if self.orientation == 'R':
            c += 1
        elif self.orientation == 'D':
            r += 1
        elif self.orientation == 'L':
            c -= 1
        elif self.orientation == 'U':
            r -= 1
        self.pos = Point(r,c)

    def __repr__(self):
        return "Position: " + str(self.pos) + " " + self.orientation


class Board:
    def __init__(self):
        self.whites = set()
        self.top_left = Point(0,0)
        self.bottom_right = Point(0,0)
        self.ant = Ant()

    def flip(self,pos):
        if pos in self.whites:
            self.whites.remove(pos)
        else:
            self.whites.add(pos)

    def update(self):
        r,c = self.ant.pos
        self.top_left = Point(min(r, self.top_left.r), min(c, self.top_left.c))
        self.bottom_right = Point(max(r, self.bottom_right.r), max(c, self.bottom_right.c))

    def play(self, k):
        print("STARTING GAME: ")
        for _ in range(k):
            self.flip(self.ant.pos)
            if self.ant.pos in self.whites:
                self.ant.turn(True)
            else:
                self.ant.turn(False)
            self.ant.move()
            self.update()
        print("FINISHED GAME:\n")

    def __repr__(self):
        result = []
        for r in range(self.top_left.c,self.bottom_right.c + 1):
            for c in range(self.top_left.r, self.bottom_right.r + 1):
                if (r,c) == self.ant.pos:
                    result.append(self.ant.orientation)
                elif (r,c) in self.whites:
                    result.append('_')
                else:
                    result.append("X")
            result.append('\n')
        print(self.ant)
        return "".join(result)

b = Board()
b.play(100)
print(b)