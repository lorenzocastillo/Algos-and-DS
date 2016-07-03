from collections import namedtuple
from itertools import chain
class Validator:
    def __init__(self, board):
        self.board = board
        self.ROWS = board.ROWS
        self.COLS = board.COLS

    def is_row_valid(self, row):
        return len({num for num in self.board[row]}) == self.ROWS

    def is_col_valid(self, col):
        return len({row[col] for row in self.board}) == self.COLS

    def is_sub_matrix_valid(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        vals = set()
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                val = self.board[i][j]
                if val in vals:
                    return False
                vals.add(val)
        return True

    def is_valid(self):
        for i in range(self.ROWS):
            valid = self.is_row_valid(i)
            if not valid:
                return False

        for j in range(self.COLS):
            valid = self.is_col_valid(j)
            if not valid:
                return False

        for start,end in self.subs:
            valid = self.is_sub_matrix_valid(start, end)
            if not valid:
                return False

        return True


class Board:

    Submatrix = namedtuple("Submatrix", 'start end')

    def __init__(self, input_board):
        self.board = list()
        self.ROWS = 9
        self.COLS = 9
        self.DIGITS = '123456789'

        board = input_board

        def initialize_board():
            k = 0
            for i in range(self.ROWS):
                self.board.append(list())
                for j in range(self.COLS):
                    self.board[i].append(board[k])
                    k += 1

        initialize_board()

        def create_submatrices():
            self.subs = list()
            for i in range(0, self.ROWS, 3):
                for j in range(0, self.COLS, 3):
                    self.subs.append(self.Submatrix(start=(i, j), end=(i + 2, j + 2)))

        create_submatrices()

        def make_unit_list():
            """
            Determines which squares belong to the same units (i.e same cols, same rows and same submatrices
            :return:
            """
            same_rows = list()
            for r in range(self.ROWS):
                row = list()
                for c in range(self.COLS):
                    row.append((r,c))
                same_rows.append(row)

            same_cols = list()
            for c in range(self.COLS):
                col = list()
                for r in range(self.ROWS):
                    col.append((r, c))
                same_cols.append(col)

            same_subs = list()
            for sub in self.subs:
                subs = list()
                for r in range(sub.start[0], sub.end[0] + 1):
                    for c in range(sub.start[1], sub.end[1] + 1):
                        subs.append((r,c))
                same_subs.append(subs)

            return same_rows + same_cols + same_subs

        unit_list = make_unit_list()
        self.squares = [(r, c) for r in range(self.ROWS) for c in range(self.COLS)]

        # creates map from square to a list of its units
        self.units = {s: [u for u in unit_list if s in u] for s in self.squares}

        # removes duplicate units and itself from its peers list
        # first it flattens the list, then makes it into a set to remove duplicates, and then it removes itself
        self.peers = {s: set(sum(self.units[s], list())) - set([s]) for s in self.squares}

    def search(self, values):
        if values is False:
            return False
        elif all(len(values[s]) == 1 for s in self.squares):
            return values
        else:
            n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
            return self.some(self.search(self.assign(values.copy(), s, d))
                        for d in values[s])

    def some(self, seq):
        for e in seq:
            if e:
                return e
        return False

    def solve(self):
        squares = self.squares
        values = {s: self.DIGITS for s in squares}
        for s in squares:
            d = self.board[s[0]][s[1]]
            if d in self.DIGITS and not self.assign(values, s, d):
                return False
        return self.search(values)

    def assign(self, values, square, digit):
        others = values[square].replace(digit, '')
        if all(self.eliminate(values, square, d2) for d2 in others):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        if digit not in values[square]:
            return values
        values[square] = values[square].replace(digit, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            d2 = values[square]
            self.board[square[0]][square[1]] = d2
            if not all(self.eliminate(values, peer, d2) for peer in self.peers[square]):
                return False

        for unit in self.units[square]:
            dplaces = [s for s in unit if digit in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], digit):
                    return False

        return values

    def __repr__(self):
        result = list()
        result.append('\n')
        for i, row in enumerate(self.board, 1):
            for j, num in enumerate(row, 1):
                result.append(str(num))
                if j % 3 == 0 and j != len(self.board):
                    result.append("|")
            result.append("\n")
            if i % 3 == 0 and i != len(self.board):
                result.append("-"*22)
                result.append("\n")
        return " ".join(result)

board = Board("""4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......""")
#board = Board("""003020600900305001001806400008102900700000008006708200002609500800203009005010300""".replace('0','.'))
print(board)
board.solve()
print(board)

#
# def cross(A, B):
#     "Cross product of elements in A and elements in B."
#     return [a+b for a in A for b in B]
#
# digits   = '123456789'
# rows     = 'ABCDEFGHI'
# cols     = digits
# squares  = cross(rows, cols)
# unitlist = ([cross(rows, c) for c in cols] +
#             [cross(r, cols) for r in rows] +
#             [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
# units = dict((s, [u for u in unitlist if s in u])
#              for s in squares)
# peers = dict((s, set(sum(units[s],[]))-set([s]))
#              for s in squares)
#
# print("Squares", squares)
# print("Unit list", unitlist)
# print("Units", units)
# print("Peers", peers)