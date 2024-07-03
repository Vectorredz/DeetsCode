def divisorSubstrings(nums: int, k:int) -> int:
    l: int = 0
    counts: int = 0
    num_list = list(str(nums))
    if len(num_list) == 1 and k == 1:
        return 1
    for r in range(len(list(str(nums)))-(k-1)):
        divisor = int(str(''.join(num_list[l:r+k])))
        if divisor != 0 and nums % divisor == 0:
            counts += 1
        l += 1
    return counts

print(divisorSubstrings(30003, 3))

def test_cases():
    assert divisorSubstrings(240, 2) == 2
    assert divisorSubstrings(430043, 2) == 2
    assert divisorSubstrings(0, 2) == 0
    assert divisorSubstrings(1000000, 3) == 1
    assert divisorSubstrings(2, 1) == 1
    assert divisorSubstrings(30003, 3) == 1
test_cases()

