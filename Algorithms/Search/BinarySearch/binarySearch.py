def search(nums: list[int], target: int):
    low: int = 0
    high: int = len(nums)-1
    while low <= high:
        midpoint = low + (high-low) // 2
        mid_value = nums[midpoint]
        if mid_value == target: 
            return midpoint
        elif target < mid_value:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return -1

def test_cases():
    assert search( [-1,0,3,5,9,12], 9) == 4
    assert search( [-1,0,3,5,9,12], 2) == -1
test_cases()