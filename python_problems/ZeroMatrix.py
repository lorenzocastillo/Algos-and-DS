def zero_matrix(matrix):
    """
    We are going to iterate through the array, and placing a 0 in the first column or row if that row/column has a 0.
    We will do a second traversal through the first row and column, and zero out the row and col
    :param matrix:
    :return:
    """
    for r in range(1,len(matrix)):
        for c in range(1,len(matrix[0])):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for row in matrix:
        print(row)
    print("\n"*2)

    def zero_row(row):
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    def zero_col(col):
        for row in range(len(matrix)):
            matrix[row][col] = 0

    for r in range(len(matrix)):
        if matrix[r][0] == 0:
            zero_row(r)

    for c in range(len(matrix[0])):
        if matrix[0][c] == 0:
            zero_col(c)

    return matrix

arr = [
    [1,   3,  3,  4],
    [5,   0,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ]

print(zero_matrix(arr))