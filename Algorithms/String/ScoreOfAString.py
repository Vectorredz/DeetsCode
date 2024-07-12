from functools import reduce

def scoreOfString(s: str) -> int:
    n = len(s)
    # s = list(map(lambda x: ord(x), s))
    total_sum: int = 0
    for r in range(1, n):
        diff = abs(ord(s[r-1]) - ord(s[r]))
        total_sum += diff
    return total_sum

def test_cases():
    assert scoreOfString("hello") == 13
    assert scoreOfString("zaz") == 50
test_cases()