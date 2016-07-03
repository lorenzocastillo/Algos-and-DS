N = 8


def check_valid(row, col, columns):
    for row2 in range(row):
        col2 = columns[row2]
        if col2 == col:
            return False
        if abs(col-col2) == abs(row-row2):
            return False
    return True


def place_queens(row, columns, results):
    if row == N:
        results.append(columns[:])
    else:
        # For every column, check if you can place a queen at (row, col), if so, place the queen there,
        # and try the next row
        for col in range(N):
            # checks to see if there's a queen in the same column or diagonal
            if check_valid(row, col, columns):
                columns[row] = col # indicates that row has a queen at column, col
                place_queens(row + 1, columns, results)

result = list()
place_queens(0, [0]*N, result)
for res in result[:1]:
    for r, c in enumerate(res):
        print(r, c)