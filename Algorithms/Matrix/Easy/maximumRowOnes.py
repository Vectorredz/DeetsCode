def rowAndMaximumOnes(mat: list[list[int]]):
    rows, cols = len(mat), len(mat[0])
    currSum = 0
    maxRet = 0
    lists = []
    hashmap: dict[int, int] = {}
    for key, val in enumerate(mat):
        currSum = sum(val)
        hashmap[key] = currSum
        maxRet = max(maxRet, currSum)

    for k, v in hashmap.items():
        if maxRet == hashmap[k]:
            lists.append(k)
    return [min(lists), maxRet]
            
def test_cases():
    assert rowAndMaximumOnes([[0,0],[1,1],[0,0]]) == [1,2]
    assert rowAndMaximumOnes([[0,0,0],[0,1,1]]) == [1,2]
    assert rowAndMaximumOnes([[0,1],[1,0]]) == [0,1]
test_cases()

