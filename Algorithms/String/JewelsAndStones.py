def numJewelsInStones(jewels: str, stones: str) -> int:
    jewels = list(jewels)
    count: int = 0
    for s in stones:
        if s in jewels:
            count += 1
    return count


print(numJewelsInStones("aA", "aAAbbbb"))

def test_cases():
    assert numJewelsInStones("aA", "aAAbbbb") == 3
    assert numJewelsInStones("z", "ZZ") == 0
    assert numJewelsInStones("", "ZZ") == 0
    assert numJewelsInStones("", "") == 0
test_cases()
    
        