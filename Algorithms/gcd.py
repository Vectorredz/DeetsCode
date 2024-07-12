# def gcd(m: int, n: int):
#     while m % n != 0:
#         m, n = n, m % n
#     return n

# print(gcd(608, 133))

def gcd(m: int, n: int):
    return (n if m % n == 0 
            else gcd(n, m % n))
    
def test_cases():
    assert gcd(10, 5) == 5
    assert gcd(608, 133) == 19
test_cases()