def modifiedMatrix(matrix: list[list[int]]):
    rows, cols = len(matrix), len(matrix[0])
    minRet: int = 0
    for col in range(cols):
        print(matrix[col])
    
    return matrix



print(modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))