"""
Given a text and a pattern, determine if the word is a match.
Ex:
Facebook, FB -> True
FooBar, FB -> True
UptownFunkYouUp, UFunYoUp -> True
UptownFunk,  UFund -> False


Note that all lowercase letters have to occur contiguously and immediately after the last upper case character.
"""
from helpers.TestSuite import Assert


def match(text, pattern):
    """
    Walk through text[i] and pattern[j].
    Determine whether pattern[j] has an upper case. If so, get the next upper case from the text, and compare. Else,
    compare pattern[j] and text[i] until pattern[j] is an upper case character.
    If we haven't found a mismatch when we have exhausted the pattern, then we are done.
    :param text:
    :param pattern:
    :return:
    """
    def get_next_upper(s, start):
        """
        determines the next occurrence of an upper case letter, or returns the length of the string
        if there are no more upper cases found.
        :param s:
        :param start:
        :return:
        """
        for i in range(start, len(s)):
            if s[i].isupper():
                return i
        return i

    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if pattern[j].isupper():
            i = get_next_upper(text, i)
            if i != len(text) and text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                return False
        else:
            while i < len(text) and j < len(pattern) and not pattern[j].isupper():
                if text[i] != pattern[j]:
                    return False
                i += 1
                j += 1
    return True


def test():
    f = match
    Assert(True, f, 'FullMatch', 'FullMatch')
    Assert(True, f, 'FaceBook', 'FB')
    Assert(True, f, 'FooBar', 'FoBa')
    Assert(True, f, 'FooBar', 'FB')
    Assert(False, f, 'FooBar', 'FaBo')
    Assert(False, f, 'FooBar', 'FosBa')
    Assert(True, f, 'myFaceBook', 'myFBook')
    Assert(False, f, 'UptownFunk', 'UFund')
    Assert(True, f, 'UptownFunk', 'UFunk')


if __name__ == '__main__':
    test()