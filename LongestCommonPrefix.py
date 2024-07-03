
def longestCommonPrefix(strs: list[str]) -> str:
    lists = []
    prefix = max(strs)
    for str in strs:
        if str[:len(prefix)] == prefix:
            lists.append(prefix)
        else:
            prefix = prefix[:-1]
    return lists


print(longestCommonPrefix(["flower","flow","flight"]))




        