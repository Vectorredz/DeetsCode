
def checkXMatrix(grid: list[list[int]]):
    rows, cols = len(grid), len(grid[0])
    flag: list[bool] = []
    for row in range(rows):
        for col in range(cols):
            if row == col:
                if grid[row][col] != 0 and grid[row][-col-1] != 0: 
                    flag.append(True)
                else:
                    flag.append(False)
            elif not grid[row][-col-1]:
                if grid[row][col] == 0:
                    flag.append(True)
                else:
                    flag.append(False)
    return all(flag)
                
print(checkXMatrix([[6,0,19],
                     [0,2,0],
                     [13,17,6]]))

def test_cases():
    assert checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]) == True
    assert checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]) == False
test_cases()