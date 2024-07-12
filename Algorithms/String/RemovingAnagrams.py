from collections import defaultdict

def removeAnagrams(words: list[str]) -> list[str]:
    hashmap = defaultdict(list)
    result = []
    new_result = []
    for word in words:
        sorted_word = tuple(sorted(word))
        hashmap[sorted_word].append(word)
    for value in hashmap.values():
        result.append(value)

    for results in result:
        new_result.append(results[0])
    return new_result

            
print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))
