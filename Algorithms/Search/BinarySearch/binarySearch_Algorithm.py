def binarySearch(s: str, target: int):
    arr_s = list(map(int, s))
    low: int = 0
    high: int = len(arr_s) - 1
    while low <= high:
        midpoint = low + (high - low) // 2
        if arr_s[midpoint] == target:
            return midpoint
        elif target < arr_s[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return None
    
print(binarySearch("123456789", 6))
# 