def maximumOddBinaryNumber(s: str) -> str:
    s = list(s)
    ret = ['0']*len(list(s))
    count = s.count('1')
    i = 0
    while count > 1:
        ret[i] = '1'
        i += 1
        count -= 1
    ret[-1] = '1'
    
    return  "".join(ret)
print(maximumOddBinaryNumber("101110"))
