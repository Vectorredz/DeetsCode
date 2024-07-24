def addToArrayForm(num: list[int], k: str):
    sum = int(''.join(list(map(str, num)))) + k
    return list(map(int, str(sum)))

def test_cases():
    assert addToArrayForm([1,2,0,0], 34) == [1,2,3,4]
    assert addToArrayForm([2,7,4], 181) == [4,5,5]
test_cases()