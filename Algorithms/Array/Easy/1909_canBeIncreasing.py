def canBeIncreasing(nums: list[int]):
    flag: bool = False
    # if len(nums) == 2:
    #     return True
    # if all(num == nums[0] for num in nums):
    #     return False
    for r in range(len(nums)-1, -1, -1):
        ret = []
        mul_arr = list(nums[:r] + nums[r+1:])
        for i in range(len(mul_arr), 1, -1):
            if mul_arr[i-1] > mul_arr[i-2]:
                ret.append(True)
            else:
                ret.append(False)
        if all(ret):
            return True
    return False

# print(canBeIncreasing([1,2,10,5,7]))
# # 3 4 5 1 5
# # 2 4 5 1 5
# # 2 3 5 1 5 
# # 2 3 4 1 5
# # 2 3 4 5 1
# # def test_cases():
# #     assert canBeIncreasing([1,2,10,5,7]) == True
# #     assert canBeIncreasing([2,3,1,2]) == False
# #     # assert canBeIncreasing([1,1,1]) == False
# #     assert canBeIncreasing([1,2,4,3]) == True
# #     assert canBeIncreasing([-1, -2]) == True
# #     assert canBeIncreasing([1,1]) == True
# #     assert canBeIncreasing([2,3,4,5,1,5]) == False
# # test_cases()
    

# def canBeIncreasing(nums: list[int]) -> bool:
#     if len(nums) == 2:
#         return True
#     if all(num == nums[0] for num in nums):
#         return False
#     for r in range(len(nums)):
#         ret = []
#         mul_arr = list(nums[:r] + nums[r+1:])
#         for i in range(len(mul_arr) - 1):
#             if mul_arr[i] < mul_arr[i+1]:
#                 ret.append(True)
#             else:
#                 ret.append(False)
#         if all(ret):
#             return True
#     return False

print(canBeIncreasing([2, 3, 4, 5, 1, 5]))  # Expected output should be True

def test_cases():
    assert canBeIncreasing([1,2,10,5,7]) == True
    assert canBeIncreasing([2,3,1,2]) == False
    assert canBeIncreasing([1,1,1]) == False
    assert canBeIncreasing([1,2,4,3]) == True
    assert canBeIncreasing([-1, -2]) == True
    assert canBeIncreasing([1,1]) == True
    assert canBeIncreasing([2,3,4,5,1,5]) == False
test_cases()