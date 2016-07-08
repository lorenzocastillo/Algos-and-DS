"""
Given a stream of chars, what's the longest substring that contains at most k distinct

abaabcb, k=1 => abc
abaabcb, k=2 => abcb or aabc

"""
from helpers.TestSuite import Assert


def longest_substring(arr, k=1):
    """
    Keep track of the last index of each character encountered. Whenever the number of distinct characters encountered
    exceeds k, we will remove the one that occurred first.
    :param arr:
    :param k:
    :return:
    """
    last = dict()
    start = 0
    longest = (start, 0)
    for i, c in enumerate(arr):
        last[c] = i

        if len(last.keys()) > k:
            letter = min(last.keys(), key=last.get)
            start = last[letter] + 1
            del last[letter]

        longest = max(longest, (start, i), key=lambda x: x[1] - x[0])

    return longest


def test():
    f = longest_substring
    Assert((4, 7), f, 'abcdaaaa', 1)
    Assert((2, 7), f, 'abadaaaa', 2)
    Assert((0, 7), f, 'abadaaaajfndkald', 3)

if __name__ == '__main__':
    test()
