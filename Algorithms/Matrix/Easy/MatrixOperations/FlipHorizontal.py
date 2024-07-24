def flipHorizontal(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    empty_matrix = [[0]*cols for _ in range(rows)]
    return matrix[::-1]

print(flipHorizontal([[11,12,21,22], 
                    [98,89,99,88], 
                    [73,37,33,77]]))