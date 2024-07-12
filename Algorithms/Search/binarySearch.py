def binarySearch(s: str, target: int):
    if len(s) % 2 != 0:
        midpoint = int(s[len(s) // 2])
        new_s = list(s[:])
        # while len(new_s) != 1:
        for _ in range(2):
            if target < midpoint:
                new_s = new_s[:(s.index(str(midpoint)))]
                midpoint = int(s[len(new_s) // 2])
            elif target > midpoint:
                new_s = new_s[(s.index(str(midpoint)))+1:]
                midpoint = int(s[len(new_s) // 2])
            
            
    return new_s, midpoint
    
print(binarySearch('12345678910',4))

# midpoint = [1]

# print(midpoint[len(midpoint) // 2])