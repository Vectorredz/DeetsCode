# def findMaxAverage(nums: list[int], k: int):
#     curAve: float = 0.0
#     maxAve: float = nums[0]

#     for r in range(len(nums)):
#         subarr: list[int] = nums[r:(r+k)%(len(nums)+1)]
#         if subarr:
#             curAve = sum(nums[r:(r+k)%(len(nums)+1)]) / k 
#             maxAve = max(maxAve, curAve)
#     return float(f"{maxAve:.5f}")

# print(findMaxAverage([1,12,-5,-6,50,3], 4))

def findMaxAverage(nums: list[int], k: int):
    curSum: int = sum(nums[:k])
    ret: int = curSum
    for r in range(len(nums)+k):
        print(r)
    #     curSum += - nums[r-k] + nums[r]
    #     ret = max(ret, curSum)
    # return ret / k 
            

print(findMaxAverage([1,12,-5,-6,50,3], 4))

def findMaxAverage(nums: list[int], k: int) -> float:
    curSum = sum(nums[:k])  # Initialize sum for the first k elements
    maxSum = curSum

    for r in range(k, len(nums)):
        curSum += nums[r] - nums[r - k]  # Slide the window
        maxSum = max(maxSum, curSum)

    return maxSum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))
# 1 12 -5 -6 == 2
# 12 -5 -6 50 == 51
# -5 -6 50 3 = 42

# 4 0 4 3 3 





# def test_cases():
#     assert findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75000
#     assert findMaxAverage([8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891], 93) == -594.58065, f"{findMaxAverage([8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891], 93) }"
# test_cases()