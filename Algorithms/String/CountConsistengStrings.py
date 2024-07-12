def countConsistentStrings(allowed: str, words: list[str]) -> int:
    allowed = list(allowed)
    count: int = 0
    for word in words:
        allowable = False
        for char in word:
            if char not in allowed:
                allowable = False
                break
            else:
                allowable = True
        if allowable:
            count += 1

    return count
        

        

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))