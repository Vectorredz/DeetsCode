def findSubarrays(nums: list[int]):
    hashmap: dict[int, int] = {}
    for r in range(len(nums)):
        if nums[r:(r+2)%(len(nums)+1)]:
            if sum(nums[r:(r+2)%(len(nums)+1)]) not in hashmap:
                hashmap[sum(nums[r:(r+2)%(len(nums)+1)])] = 1
            else:
                hashmap[sum(nums[r:(r+2)%(len(nums)+1)])] += 1
    flag: bool = False
    for values in hashmap.values():
        if values >= 2:
            flag = True
            break
        else:
            flag = False
    return flag
print(findSubarrays([77,95,90,98,8,100,88,96,6,40,86,56,98,96,40,52,30,33,97,72,54,15,33,77,78,8,21,47,99,48]))