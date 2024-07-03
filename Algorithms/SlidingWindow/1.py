# lst = [1,2,3,4,5,6]
# k = 2

# def fixedSlidingWindow(lst: list[int], k:int):
#     result: list[int]= []
#     for i in range(len(lst)):
#         result.append(lst[i:k+i])
#     return result
        
# print(fixedSlidingWindow(lst, k))


def maximumSubArray(arr: list[int], k: int):
    sum_list: list[int] = []
    if len(arr) > k:
        for i in range(len(arr)):
            sum_list.append(sum(arr[i:k+i]))
        return max(sum_list)
    
def maximumSubArray(arr: list[int], k:int):
    lst = [arr[i:k+i] + [0] if len(arr[i:k+i]) <= 1 else arr[i:k+i] for i in range(len(arr))]
    return max(list(map(lambda x: sum(x), lst)))

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
def maximumSubArray(arr: list[int], k: int, n: int):
    
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
    max_sum = max(current_sum, max_sum)
    
    return 



print(maximumSubArray(arr, k, n))
# assert maximumSubArray([100, 200, 300, 400], 2) == 700
# assert maximumSubArray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

