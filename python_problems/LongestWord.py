"""
Given a list of words, write a program to find the longest word made of other words in the list.
"""


def longest_word(words):
    """
    We first start by sorting the list of words by size from longest to smallest. We include all the words in the cache
    as cache[word] = True to indicate that we have seen them and they are valid words. Then, we check each word to see if
    the word could be made up of other words.
    We do this by first checking the left side of a word and see if it's a word, and recursively checking the right side,
    to make sure if that's a word made up of other words. If it is, we return True, else we make the left side bigger and
     repeat.
     The one thing we need to make sure is that a word needs to be made up of OTHER words, not itself, or else the answer
     would always be the longest word in the list. We take this into account by passing in the is_original parameter
    :param words: the list of words we are searching for
    :return: the longest word made of other words in the list
    """
    cache = dict()

    def can_build_word(w, original_w=False):
        if not original_w and w in cache:
            return cache[w]
        else:
            for i, c in enumerate(w):
                left = w[:i]
                right = w[i:]
                if left in cache and cache[left] == True and can_build_word(right):
                    return True
            cache[w] = False
            return False

    words = sorted(words, key=lambda x: -len(x))

    for word in words:
        cache[word] = True

    for word in words:
        if can_build_word(word, True):
            return word

    return None

arr = ['cat','nana', 'ba', 'dogwalker','dog','walk','walker', 'banana']
print(longest_word(arr))
