def flipAndInvertImage(image: list[list[int]]):
    rows = len(image)
    cols = len(image[0])
    new_list = [[0 for _ in range(rows)]for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            if image[r][::-1][c] == 1:
                new_list[r][c] = 0
            elif image[r][::-1][c] == 0:
                new_list[r][c] = 1
    return new_list


print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

