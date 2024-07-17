def maximumWealth(accounts: list[list[int]]):
    currSum: int = 0
    maxRet: int = 0
    for i in range(len(accounts)):
        currSum += sum(accounts[i])
        maxRet = max(maxRet, currSum)
        currSum = 0
    return maxRet
        
print(maximumWealth([[1,5],[7,3],[3,5]]))