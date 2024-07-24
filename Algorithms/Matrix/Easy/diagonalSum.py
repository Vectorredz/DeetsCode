def diagonalSum(mat: list[list[int]]):
    currSum = 0
    center = len(mat) // 2
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                currSum += mat[i][j] + mat[i][-j-1]
    if len(mat[0])  % 2 != 0 and len(mat) % 2 != 0:
        return currSum - mat[center][center]
    else:
        return currSum
    
print(diagonalSum([[1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]]))

