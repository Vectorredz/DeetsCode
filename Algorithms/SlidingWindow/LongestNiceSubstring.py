def is_nice(substr):
    if all(str.upper() in substr and str.lower() in substr for str in substr):
        return True
    return False

def longestNiceSubstring(s: str):
    nice = []
    for i in range(len(s)):
        for j in range(i, len(s)): 
            substr = s[i:j+1]
            if is_nice(substr):
                nice.append(substr)
    if nice:
        res = max(list((lambda x: x)(nice)), key=len) 
        return res
    return ''
        

print(longestNiceSubstring("YazaAay"))