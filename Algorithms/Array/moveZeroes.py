def moveZeroes(nums: list[int]) -> None:
    for num in nums:
        if num == 0:
            nums.pop(nums.index(num))
            nums.append(0)
        print(num)
    return nums

print(moveZeroes([0,1,0,3,12]))