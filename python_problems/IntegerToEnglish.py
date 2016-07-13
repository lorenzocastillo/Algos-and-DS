"""
Given an integer from -9,999,999,999 to 9,999,999,999, covert to the english translation.  For example,
19,000,499 -> nineteen million four hundred ninety nine

Sketch of Algorithm:
if num == 0:
    return 0
else if negative
    pre-pend 'negative' and continue:
else
    break num into chunks of three digits.
    For example,
        176,930 -> 176 and 930
    for each chunk, convert to their english translation and
    append the required place value (e.g millions, thousands... ). In our case, we will go from
    right to left of the numbers, and appendLeft on a list.
        list = []
        930 -> nine hundred thirty -> list = ['nine hundred thirty']
        176 -> one hundred seventy six + thousand -> list = ['one hundred seventy six thousand', 'nine hundred thirty']
    When we finish, we print the results of the list.
"""
from helpers.TestSuite import Assert
from collections import deque

smalls = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine','ten', 'eleven', 'twelve',
          'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
bigs = ['', 'thousand', 'million','billion']
hundred = 'hundred'
negative = 'negative'


def __convert_chunk(num):
    if num >= 100:
        return smalls[num//100] + ' ' + hundred + ' ' + __convert_chunk(num % 100)
    elif 10 <= num < 20:
        return smalls[num]
    elif num >= 20:
        return tens[num//10] + ' ' + __convert_chunk(num % 10)
    else:
        if num == 0:
            return ''
        return smalls[num]


def int_to_eng(num):
    if num == 0:
        return smalls[0]
    elif num < 0:
        return negative + ' ' + int_to_eng(-1 * num)
    else:
        result = deque()
        n_chunks = 0
        while num > 0:
            part = num % 1000
            if part != 0:
                result.appendleft(__convert_chunk(part) + " " + bigs[n_chunks])
            num //= 1000
            n_chunks += 1

        return " ".join(result).strip()


def test():
    cc = int_to_eng
    Assert('zero',cc, 0)
    Assert('one', cc, 1)
    Assert('thirteen', cc, 13)
    Assert('four hundred forty five', cc, 445)
    Assert('five hundred sixteen', cc, 516)
    Assert('forty three', cc, 43)
    Assert('nine', cc, 9)
    Assert('nineteen million', cc, 19000000)
    Assert('five hundred thirty two thousand', cc, 532000)
    Assert('nine hundred sixty five', cc, 965)
    Assert('nineteen million five hundred thirty two thousand nine hundred sixty five', cc, 19532965)

if __name__ == '__main__':
    test()