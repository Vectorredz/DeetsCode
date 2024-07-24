def decompressRLElist(nums: list[int]):
    ret: list[int] = []
    # for i in range(0, len(nums), 2):
    #     arr = nums[i:i+2]
    #     key, val = arr[0], arr[1]
    #     ret += key * [val]

    i = 0
    while i < len(nums)-1:
        arr = nums[i:i+2]
        key, val = arr[0], arr[1]
        ret += key * [val]
        i += 2
    return ret
    
print(decompressRLElist([1,2,3,4]))