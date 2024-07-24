def largestTriangleArea(points: list[list[int]]):
    x_val: int= 0
    y_val: int = 0
    x_maxRet: int = 0
    y_maxRet: int = 0

    for i in range(len(points)):
        x_val = points[i][0]
        y_val = points[i][1]
        x_maxRet, y_maxRet = max(x_maxRet, x_val), max(y_maxRet, y_val)

    return 1/2 * (x_maxRet * y_maxRet)
print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))