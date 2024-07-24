def flip_NE(matrix):
    rows, cols = len(matrix), len(matrix[0])
    empty_row = [[0]*rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            empty_row[col][row] = matrix[::-1][row][col]
    return empty_row[::-1]

print(flip_NE([[11,12,21,22], 
                    [98,89,99,88], 
                    [73,37,33,77]]))