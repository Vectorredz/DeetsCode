def move_d(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    d = matrix.pop(0)
    matrix.append(d)
    return matrix
print(move_d([[11,12,21,22], 
            [98,89,99,88], 
            [73,37,33,77]]))
    