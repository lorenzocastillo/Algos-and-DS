from collections import namedtuple

class Submatrix:
    def __init__(self, up, down, left, right, val):
        self.top_left = (up, left)
        self.top_right = (up, right)
        self.bottom_left = (down, left)
        self.bottom_right = (down, right)
        self.value = val

    def __repr__(self):
        res = [self.top_left, self.top_right, self.bottom_left, self.bottom_right, self.value]
        return res.__repr__()

def max_subarray(arr):
    cur_sum = 0
    start = 0
    Range = namedtuple("Range","start end value")
    best_range = Range(0,0,0)
    for i in range(start, len(arr)):
        cur_sum += arr[i]

        if cur_sum < 0:
            cur_sum = 0
            start = i + 1

        best_range = max(best_range, Range(start, i, cur_sum), key=lambda x: x.value)

    return best_range

def max_submatrix(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    best_submatrix = None

    for row_start in range(n_rows):
        partial_sum = [0]*n_cols
        for row_end in range(row_start, n_rows):
            for col in range(n_cols):
                partial_sum[col] += matrix[row_end][col]

            best_range = max_subarray(partial_sum)
            if best_submatrix is None or best_range.value > best_submatrix.value:
                best_submatrix = Submatrix(row_start, row_end, best_range.start,best_range.end, best_range.value)

    return best_submatrix

matrix = [
            [9, -8, 1, 3],
            [-3, 7, 6, 4],
            [6, -4, -4, -7],
            [12, -5, 3, -5]
        ]

