def thirdMax(nums: list[int]): 
    distinct = set(nums)
    if (len(distinct)-1) >= 2:
        return sorted(list(distinct))[-3]
    elif (len(distinct)-1) < 2 and (len(distinct)-1) > 0:
        return sorted(list(distinct))[-1]
    else:
        return []
    
        
print(thirdMax([]))