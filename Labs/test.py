arr = [[1,2,3], [2,3,4]]
ret = list(filter(lambda x: x[0] if x[0] == 1 else '', arr))

print(ret)