def minimumDifference(nums: list[int], k: int):
    n: int = len(nums)
    ret: int = max(nums)
    if len(nums) <= 1:
        return 0
    for i in range(n):
        if sorted(nums)[i:(i+k)%(n+1)]:
        # maxx = max(sorted(nums)[i:(i+k)%n])
        # minn = min(sorted(nums)[i:(i+k)%n])
          maxx = max(sorted(nums)[i:(i+k)%(n+1)])
          minn = min(sorted(nums)[i:(i+k)%(n+1)])
          diff = abs(maxx - minn)
          ret = min(ret, diff)
    return ret

print(minimumDifference([93614,91956,83384,14321,29824,89095,96047,25770,39895], 3))

