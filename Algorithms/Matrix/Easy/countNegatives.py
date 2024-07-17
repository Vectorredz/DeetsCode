def countNegatives(grid: list[list[int]]):
    # rows, cols = len(grid)-1, len(grid[0])
    lists = []
    count: int = 0
    maxRet: int = 0
    for i in range(len(grid)):
        sorted_row = sorted(grid[i])
        l: int = 0
        r: int = len(sorted_row)-1
        while l <= r:
            midpoint = l + (r-l) // 2
            midvalue = sorted_row[midpoint]
            if midvalue < 0:
                count = midpoint + 1
                l = midpoint + 1
            else:
                r = midpoint - 1 
        maxRet += count
    return maxRet

print(countNegatives([[1,2,-1],[1,2,-2]]))