def binaryToDecimalConverter(s: str):
    bin = []
    for i in range(len(s)-1, -1, -1):
        bin.append(((2 ** i) *  int(s[::-1][i])))
    return sum(bin)

print(binaryToDecimalConverter('1011110'))

def binaryToDecimalConverter(s: str):

    sums = 0
    for i in range(len(s)):
        ret = (2 * sums) + int(s[i])
        sums = ret
    return ret

print(binaryToDecimalConverter('1110'))

def binaryToDecimalConverter(s: str):
    if not s: 
        return 0
    else:
        return (2 * binaryToDecimalConverter(s[:-1])) + int(s[-1])

# 2 * sum + 1 = 11
# 2 * sum + 1 = 5
# 2 * sum + 0 = 2
# 2 * sum + 1 = 1
    
print(binaryToDecimalConverter('1101'))