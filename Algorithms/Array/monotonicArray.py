def isMonotonic(nums: list[int]):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        return True
    else:
        return False

print(isMonotonic([1,2,2,3]))