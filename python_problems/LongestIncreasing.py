"""
Given a list of numbers, find the longest "increasing by one" subarray. What if you're allowed 1 mistake?
"""
from collections import namedtuple


def longest_increasing(arr):
    start = 0
    longest = (start,0)
    for i in range(1, len(arr)):
        if arr[i - 1] + 1 != arr[i]:
            start = i + 1
        longest = max(longest, (start, i), key=lambda x: x[1] - x[0])

    return longest


def longest_increasing_mistake(arr, m=1):
    Range = namedtuple('Range', 'start end last_valid')
    longest = Range(0, 0, 0)
    cur = 1
    prev = Range(0, 0, arr[0])
    mistakes = 0
    last_mistake = 1
    while cur < len(arr):
        if prev.last_valid + 1 != arr[cur]:
            mistakes += 1
            if mistakes > m:
                mistakes = 1
                prev = Range(last_mistake + 1, cur, arr[cur - 1])
            last_mistake = cur
            prev = Range(prev.start, cur, prev.last_valid)
        else:
            prev = Range(prev.start, cur, arr[cur])
        longest = max(prev, longest, key=lambda x: x[1] - x[0])
        cur += 1
    return longest[:2]


print(longest_increasing_mistake([2, 3, 4, -9, 5, 6, -2, 7, 8, 9, 10, 11]))
