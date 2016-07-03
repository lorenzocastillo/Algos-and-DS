def rotate(matrix):
    """
    To rotate the matrix, we will rotate all four corners at a time. We will iterate from 0 to N/2 since we are doing
    two swaps per iteration. We also need to decrement the 'last' position at each iteration to make the layers smaller.
    We will then iterate from first to last and performing the swap operations. 
    :param matrix:
    :return:
    """
    N = len(matrix)

    for first in range(N//2):
        last = N - 1 - first
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # bottom-left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom-right -> bottom-left
            matrix[last-offset][first] = matrix[last][last-offset]

            # top-right -> bottom-left
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return matrix

arr = [
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
    ]

print(rotate(arr))