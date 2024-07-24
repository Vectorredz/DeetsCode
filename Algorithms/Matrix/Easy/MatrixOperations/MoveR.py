def move_r(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        r = matrix[row].pop(0)
        matrix[row].append(r)
    return matrix
print(move_r([[11,12,21,22], 
            [98,89,99,88], 
            [73,37,33,77]]))