# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Method 1: Combinations
# from itertools import combinations

# def twosum(nums: list[int], target: int):
#     indices: list[int]= []
#     for i in list(combinations(nums, 2)):
#         if sum(i) == target:
#             if i[0] == i[1]:
#                 for key, value in enumerate(i):
#                     indices.append(key)
#                 return indices
#             else:
#                 return [nums.index(i[0]), nums.index(i[1])]
        
# Method 2: Hashmap
# 3 2 4 iff 6
# 6 - 3 = 3 -> key 0 but should not be the same 
# 6 - 2 = 4 -> key 1 so [1,2]
# 6 - 4 = 2 -> key 2 so [2,1]

def twosum(nums: list[int], target: int):
    hash: dict[int, int] = {}
    for key, val in enumerate(nums):
        diff = target - val
        if diff not in hash:
            hash[val] = key
        elif diff in hash:
            return [hash[diff], key]
            

def test_twosum():
    assert twosum([2,7,11,15], 9) == [0,1], f"{twosum([2,7,11,15], 9)}"
    assert twosum([3,2,4], 6) == [1,2], f"{twosum([3,2,4], 6)}"
    assert twosum([3,3], 6) == [0,1], f"{twosum([3,3], 6)}"
test_twosum()
