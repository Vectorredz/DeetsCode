def isCircularSentence(sentence: str) -> bool:
    words: list[str] = []
    j: int = 0
    flag: bool
    for i in range(len(sentence)):
        if sentence[i] == ' ' or (i+1) == len(sentence):
            words.append(sentence[j:i+1].strip())
            j = i+1
    reversed_words = list(reversed(words))
    for r in range(len(reversed_words)):
        if len(words) > 1:
            if reversed_words[r-1][0] != reversed_words[r][-1]:
                flag = False
                break
            else:
                flag = True
        elif len(reversed_words) == 1:
            if words[r][-1] == words[r][0]:
                flag = True
        else:
            flag = False
    return flag
        
print(isCircularSentence("MuFoevIXCZzrpXeRmTssj lYSW U jM"))


# def test_cases():
#     assert isCircularSentence("leetcode exercises sound delightful") == True
#     assert isCircularSentence("eetcode") == True
#     assert isCircularSentence("Leetcode is cool") == False
# test_cases()