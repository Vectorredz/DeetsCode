def decrypt(code: list[int], k: int):
    crosscode: list[int] = code[:]
    results: list[int] = []
    # rotate to the left if k is negative
    for i in range(len(code)):
        crosscode = code[i:] + code[:i]
        if k < 0:
            results.append(sum(crosscode[k:]))
        elif k > 0:
            results.append(sum(crosscode[1:k+1]))
        elif k == 0:
            return len(code) * [0]
    return results


def test_decript():
    assert  decrypt([2,4,9,3], -2) == [12,5,6,13]
    assert  decrypt([5,7,1,4], 3) == [12,10,16,13], f"{decrypt([5,7,1,4], 3)}"
    assert  decrypt([1,2,3,4], 0) == [0,0,0,0], f"{decrypt([1,2,3,4], 0)}"
test_decript()

# 5 -> 7 + 1 + 4
# 7 -> 5 + 1 + 4
# 1 -> 4 + 5 + 7
# 4 -> 5 + 7 + 1

# 2 -> 3 + 9
# 4 -> 2 + 3
# 9 -> 2 + 4
# 3 -> 9 + 4