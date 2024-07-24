def transpose(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    empty_matrix = [[0]*rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            empty_matrix[col][row] = matrix[row][col]
    return empty_matrix
           

print(transpose([[1,2,3],[4,5,6], [3,6,9]]))
# [[1,4,7],
# [2,5,8],
# [3,6,9]]dw

# [[1,2,3]
# [4,5,6]]