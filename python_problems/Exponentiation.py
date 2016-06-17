def power(base,exp):
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

print(power(2,8))
print(power(2,5))
print(power(2,-6))

import timeit
setup = """
import sys

value = sys.maxsize
"""
t = timeit.Timer(stmt='value & 1 == 0',setup=setup).timeit(number=1000000)
print(t)
t = timeit.Timer(stmt='value % 2 == 0',setup=setup).timeit(number=1000000)
print(t)
