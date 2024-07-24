def maximumValue(strs: list[str]) -> int:
    ret: int = 0
    maxRet: int = 0
    for r in strs:
        try:
            if int(r):
                ret = int(r)
        except:
            ret = len(r)
        maxRet = max(maxRet, ret)
    return maxRet

def test_cases():
    assert maximumValue(["alic3","bob","3","4","00000"]) == 5
    assert maximumValue(["1","01","001","0001"]) == 1
test_cases()

# Solution #2 
def maximumValue(strs: list[str]) -> int:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    maxRet: int = 0
    for r in strs:
        if any(n in letters for n in list(r)):
            ret = len(r)
        else:
            ret = int(r)
        maxRet = max(maxRet, ret)
    return maxRet