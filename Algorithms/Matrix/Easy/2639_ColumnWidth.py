def findColumnWidth(grid: list[list[int]]):
    rows, cols = len(grid), len(grid[0])
    maxCol: int = 0
    ret: list[int] = []
    for col in range(cols):
        maxRet: int = 0
        for row in range(rows):
            maxCol = len(str(grid[row][col]))
            maxRet = max(maxRet, maxCol)
        ret.append(maxRet)
    return ret
    
def test_cases():
    assert findColumnWidth([[1],[22],[333]]) == [3]
    assert findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]) == [3,1,2]
test_cases()