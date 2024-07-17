def maxSubArray(nums: list[int]):
    # if len(nums) <= 2:
    #     return max(nums)
    maxSum = nums[0]
    currSum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            currSum = sum(nums[i:j+1])
            if currSum < 0:
                currSum = 0
            maxSum = max(maxSum, currSum)
    return maxSum

def test_cases():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23
    assert maxSubArray([1,2]) == 3
test_cases()