def maxSubnumsaySumCircular(nums: list[int]):
    currSum = 0
    maxSum = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(nums[i:(j+1)] + nums[j:(i)])
            # currSum = sum(nums[i:(j+1)%(len(nums)+1)] + nums[j:(i+1)%(len(nums)+1)])
            # maxSum = max(maxSum, currSum)
    return maxSum
print(maxSubnumsaySumCircular([5, -3, 5]))


"""
5 -3 + 
"""

"""
1
1 -2 
1 -2 3 
1 -2 3 -2 
-2 1
-2
-2 3 
-2 3 -2
-2 1
3 -2 
-2 1
"""

# def test_cases():
#     assert maxSubnumsaySumCircular([1,-2,3,-2]) == 3
#     assert maxSubnumsaySumCircular([5,-3,5]) == 10
#     assert maxSubnumsaySumCircular([-3,-2,-3]) == -2
# test_cases()
