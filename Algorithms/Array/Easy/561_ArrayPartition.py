def arrayPairSum(nums: list[int]):
    ret: list[list[int]] = []
    nums.sort()
    i: int = 0
    count: int = 0
    count1: int = 0
    while i <= len(nums)-1:
        count += nums[i]
        i += 2
    for i in range(0, len(nums),2):
        count1 += nums[i]
        print(count1)
    return count1

print(arrayPairSum([6,2,6,5,1,2]))