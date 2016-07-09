from enum import Enum
from random import shuffle, randrange
DEBUG = True

class CellType(Enum):
    none = 1
    number = 2
    mine = 3

class Cell:

    def __init__(self):
        self.is_flagged = False
        self.is_exposed = False
        self.value = 0
        self.type = CellType.none

    def is_mine(self):
        return self.type == CellType.mine

    def is_num(self):
        return self.type == CellType.number

    def flip(self):
        self.is_exposed = True

    def __repr__(self):
        if self.is_exposed or DEBUG:
            if self.type is CellType.mine:
                return '*'
            else:
                return '_' if self.value == 0 else str(self.value)
        else:
            return '?'

class Board:

    def __init__(self, n, b):
        self.board = [[Cell() for r in range(n)] for c in range(n)]
        self.cells = [(r,c) for r in range(n) for c in range(n)]
        self.n = n
        self.b = b
        self.game_started = False

    def expose(self, r, c):
        def flip_adjs(row, col):
            for nr, nc in self.get_adjs(row, col):
                adj = self.board[nr][nc]
                if not adj.is_exposed:
                    adj.flip()
                    if adj.value == 0:
                        flip_adjs(nr, nc)

        if not self.game_started:
            self.game_started = True
            self.set_bombs((r, c))

        if self.board[r][c].is_mine():
            return True
        elif self.board[r][c].value == 0:
            self.board[r][c].flip()
            flip_adjs(r, c)
        else:
            self.board[r][c].flip()

        return False

    def get_adjs(self, r, c):
        deltas = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        for dr, dc in deltas:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < self.n and \
               0 <= nc < self.n and \
               not self.board[nr][nc].is_mine():
                yield nr, nc

    def set_bombs(self, start):

        def choose(b):
            row, col = start

            last = len(self.cells) - 1
            for nr, nc in self.get_adjs(row, col):
                i = nr * self.n + nc
                self.cells[i], self.cells[last] = self.cells[last], self.cells[i]
                last -= 1

            i = row * self.n + col
            self.cells[i], self.cells[last] = self.cells[last], self.cells[i]

            for i in range(last):
                rand = randrange(i, last)
                self.cells[i], self.cells[rand] = self.cells[rand],self.cells[i]

            for r, c in self.cells[:b]:
                self.board[r][c].type = CellType.mine
                increment(r, c)

            return self.cells

        def increment(r, c):
            for nr, nc in self.get_adjs(r, c):
                adj = self.board[nr][nc]
                adj.type = CellType.number
                adj.value += 1

        choose(self.b)

    def __repr__(self):
        n = self.n
        board = list('\n')
        for r in range(n):
            for c in range(n):
                board.append(self.board[r][c].__repr__())
            board.append('\n')
        return " ".join(board)


def test():
    b = Board(7, 7)
    b.expose(4, 3)
    print(b)
    print('-' * 10)
    global DEBUG
    DEBUG = False

    print(b)
    print('-' * 10)
    gameover = False
    while not gameover:
        r = int(input("Enter Row: "))
        c = int(input("Enter Col: "))
        gameover = b.expose(r, c)
        print('-'*10)
        print(b)

    print(gameover)


if __name__ == '__main__':
    test()
