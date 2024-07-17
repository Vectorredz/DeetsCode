def twoSum(numbers: list[int], target: int):
    l, r = 0, len(numbers)-1
    while l <= r:
        if numbers[r] + numbers[l] == target:
            return [l+1, r+1]
        elif numbers[r] + numbers[l] > target:
            r -= 1
        else:
            l += 1
    
print(twoSum([2,7,11,15], 9))