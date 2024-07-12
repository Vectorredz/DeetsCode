def findLHS(nums: list[int]):
    n: int = len(nums)
    l: int = 0
    total = 0
    ret: int = 0
    hashmap = {}
    for r in range(len(nums)):
        if nums[r] not in hashmap:
            hashmap[nums[r]] = 1
        else:
            hashmap[nums[r]] += 1

    for num, count in hashmap.items():
        if num + 1 in hashmap:
            total = hashmap.get(num) + hashmap.get(num+1) 
        ret = max(ret, total)
    return ret
        

print(findLHS([1,3,2,2,5,2,3,7]))
    