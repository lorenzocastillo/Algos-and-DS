"""
Given a Tic-Tac-Toe board, determine if it's game over
"""


def is_game_over(board, empty=' '):
    ROWS = len(board)
    COLS = len(board[0])

    def all_in_a_row():
        return any(all(board[r][c] == board[r][0] and board[r][0] != empty for c in range(COLS)) for r in range(ROWS))

    def all_in_a_col():
        return any(all(board[r][c] == board[0][c] and board[0][c] != empty for r in range(ROWS)) for c in range(COLS))

    def all_diag():
        return all(board[i][i] == board[0][0] and board[0][0] != empty for i in range(ROWS)) or \
               all(board[ROWS - i - 1][i] == board[-1][0] and board[-1][0] != empty for i in range(ROWS))

    return all_in_a_row() or all_in_a_col() or all_diag()

board = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

print(is_game_over(board))