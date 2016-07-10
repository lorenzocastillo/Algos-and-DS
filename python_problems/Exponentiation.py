"""
Given a base and an exponent, write a power function.
"""
from helpers.TestSuite import Assert

def power(base, exp):
    is_negative = False
    if exp < 0:
        is_negative = True
        exp = -exp

    def __power(a,b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        else:
            if b % 2 == 0:
                x = __power(a, b/2)
                return x * x
            else:
                return a * __power(a, b -1)

    result = __power(base, exp)
    if is_negative:
        return 1/result
    else:
        return result

def test():
    assert pow(2, 8) == power(2, 8)
    assert pow(2, 5) == power(2, 5)
    assert pow(2, -6) == power(2, -6)
    print("All tests passed. ")

if __name__ == '__main__':
    test()
