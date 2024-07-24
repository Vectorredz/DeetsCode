def flipVertical(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    empty_matrix = [[0]*cols for _ in range(rows)]
    for row in range(rows):
        empty_matrix[row] = matrix[row][::-1]
    return empty_matrix

print(flipVertical([[11,12,21,22], 
                    [98,89,99,88], 
                    [73,37,33,77]]))