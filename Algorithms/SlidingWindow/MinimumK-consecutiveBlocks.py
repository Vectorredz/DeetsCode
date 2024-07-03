import pprint
# Solution 1: For loop method
# def minimumRecolors(blocks: str, k: int):
#     count: int = 0
#     block_lists: list[str] = list(blocks)
#     n = len(block_lists)
#     substrings: list[list[str]] = []
#     if k < 1:
#         return 0
#     for r in range(n):
#         if block_lists[r:(r+k)%(n+1)]:
#             substrings.append(block_lists[r:(r+k)%(n+1)])
#     recolor_blocks = max(substrings, key=lambda x: x.count('B'))
#     for i in recolor_blocks:
#         if i == 'W' and recolor_blocks.count('B') != k:
#             count += 1
#             i = 'B'
#     return count

# Solution 2: 
def minimumRecolors(blocks: str, k: int):
    ret = []
    block_lists: list[str] = list(blocks)
    n = len(block_lists)
    # substrings: list[list[str]] = []
    if k < 1:
        return 0
    for r in range(n):
        if block_lists[r:(r+k)%(n+1)]:
            substring: list[str] = block_lists[r:(r+k)%(n+1)]
            ret = max(ret, substring, key=lambda x: x.count('B'))
    if ret == []:
        return k
    return ret.count('W')

print(minimumRecolors("WBB", 1))


    # recolor_blocks = max(substrings, key=lambda x: x.count('B'))
    # for i in recolor_blocks:
    #     if i == 'W' and recolor_blocks.count('B') != k:
    #         count += 1
    #         i = 'B'
    # return count


def test_cases():
    assert minimumRecolors("WBBWWBBWBW", 7) == 3
    assert minimumRecolors("WBWBBBW", 2) == 0, minimumRecolors("WBWBBBW", 2)
    assert minimumRecolors("BBBB", 2) == 0
    assert minimumRecolors("WWWWW", 2) == 2, minimumRecolors("WWwWW", 2)
    assert minimumRecolors("W", 0) == 0
    assert minimumRecolors("BWBBWWBBBWBWWWBWWBBWBWBBWBB", 11) == 4, minimumRecolors("BWBBWWBBBWBWWWBWWBBWBWBBWBB", 11)
test_cases()