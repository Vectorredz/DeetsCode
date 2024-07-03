# good - distinct characters with k = 3

# Solution 1: O(N) with helper function

def distinctSubstring(s: str):
    filter = []
    for i in s:
        if i not in filter:
            filter.append(i)
        else:
            return False
    if len(filter) == 3:
        return filter
    else:
        return False
        
def countGoodSubstrings(s: str):
    count = 0
    k = 3
    s = list(s)
    for i in range(len(s)):
        str = s[i:k+i]
        if distinctSubstring(str):
            count += 1
        else:
            count = count
    return count


# Solution 2: 

def countGoodSubstrings1(s: str):
    count = 0
    k = 3
    for i in range(len(s)-2):
        if len(set(s[i:i+k])) == 3:
            count += 1
    return count
print(countGoodSubstrings1('aababcabc'))


