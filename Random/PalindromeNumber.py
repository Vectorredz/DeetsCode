def isPalindrome(x: int):
    k = list(map(str, str(x)))
    if k[:] == k[::-1]:
        return True
    return False
print(isPalindrome(121))

def test_isPalindrome():
    assert isPalindrome(121) == True
    assert isPalindrome(-121) == False
    assert isPalindrome(10) == False
    assert isPalindrome(0) == True
test_isPalindrome()
    
