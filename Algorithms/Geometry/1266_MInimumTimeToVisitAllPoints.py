def minTimeToVisitAllPoints(points: list[list[int]]):
    maxRet = 0
    # max(x2-x1, y2-y1)
    
    for i in range(len(points)-1):
        x1, x2, y1, y2 = points[i:i+2][0][0], points[i:i+2][1][0], points[i:i+2][0][1], points[i:i+2][1][1]
        currRet_x = abs(x2 - x1)
        currRet_y = abs(y2 - y1)
        currRet = max(currRet_x, currRet_y)
        maxRet += currRet
    return maxRet

def test_cases():
    assert minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) == 7
    assert minTimeToVisitAllPoints([[3,2],[-2,2]]) == 5
test_cases()