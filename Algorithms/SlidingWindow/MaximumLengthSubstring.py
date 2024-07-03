import collections

def maximumLengthSubstring(s: str):
    charset = collections.deque([])
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charset and charset.count(s[r]) >= 2:
            charset.popleft()
            l += 1
        charset.append(s[r])
        res = max(res, r + 1 - l)
    return res

print(maximumLengthSubstring("aaaa"))
# def test_cases():
#     # assert maximumLengthSubstring("bcbbbcba") == 4
#     # assert maximumLengthSubstring("aaaa") == 2
#     # assert maximumLengthSubstring("aa") == 2
#     # assert maximumLengthSubstring("bcbbbcba") == 5
# # test_cases()