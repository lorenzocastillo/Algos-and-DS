from bisect import *

T = 'banana'


def build_suffix_array(T):
    return sorted([T[i:] for i, _ in enumerate(T)])

suffix_array = build_suffix_array(T)
print(suffix_array)
