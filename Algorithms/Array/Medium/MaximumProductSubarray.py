from functools import reduce

# def maxProduct(nums: list[int]):
#     if len(nums) == 1:
#         return nums[0]
#     maxProd = 0
#     currProd = 1
#     for r in range(len(nums)):
#         print(nums[r:], currProd)
#         currProd = reduce(lambda x, y: x * y, nums[r:])
#         maxProd = max(maxProd, currProd)
#     return maxProd

def maxProduct(nums: list[int]):
    curMin, curMax = 1, 1
    curProd = nums[0]
    for r in nums:
        val = (r, curMin * r, curMax * r)
        curMin, curMax = min(val), max(val)
        curProd = max(curProd, curMax)
    return curProd

# def maxProduct(nums):
#     maxRet = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             ret = reduce(lambda x,y: x * y,nums[i:j+1])
#             maxRet = max(maxRet, ret)
#     return maxRet


print(maxProduct([2,-5,-2,-4,3]))
def test_cases():
    assert maxProduct([2,3,-2,4]) == 6
    assert maxProduct([-2,0,-1]) == 0
    assert maxProduct([-1]) == -1
    assert maxProduct([2,-5,-2,-4,3]) == 24
test_cases()