def flip_se(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    empty_row = [[0]*rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            empty_row[col][row] = matrix[row][col]
    return empty_row

print(flip_se([[11,12,21,22], 
                    [98,89,99,88], 
                    [73,37,33,77]]))