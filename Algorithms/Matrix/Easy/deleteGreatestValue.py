def deleteGreatestValue(grid: list[list[int]]):
    rows = len(grid)
    cols = len(grid[0])
    sumRet = 0
    while len(grid[0]) > 0:
        currMax = 0
        iterMax = 0
        for r in range(rows):
            currMax = max(grid[r])
            iterMax = max(iterMax, currMax)
            grid[r].pop(grid[r].index(currMax))
        sumRet += iterMax
    return sumRet

 


        
print(deleteGreatestValue([[1,2,4],[3,3,1]]))
