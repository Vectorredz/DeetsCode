def rotateString(s: str, goal: str) -> bool:
    arr_s = list(s)
    shift: int = 0
    for _ in range(len(s)):
        elem = arr_s.pop(-1)
        arr_s.insert(0, elem)
        shifted_arr = arr_s
        shift += 1
        if "".join(shifted_arr) == goal:
            return True
    return False
print(rotateString("abcde", "cdeab"))

        