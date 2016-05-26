"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they
are one edit (or zero edits) away
"""


def solution(str1, str2):
    """

    :param str1:
    :param str2:
    :return:
    """
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    if len(str1) - len(str2) > 1:
        return False # impossible for it to be distance one away if their lengths differ by more than 1

    for i, _ in enumerate(str2):
        if str1[i] != str2[i]:
            return str1[i + 1:] == str2[i:]

    return True

def test():
    inputs_a = ['ab','ba','abc','abcd', 'abc','','','abcdef']
    inputs_b =['a','a','abcd','abc','abc','','a','a']
    answers = [True, True, True, True, True, True, True, False]
    for i, input_ in enumerate(zip(inputs_a,inputs_b)):
        str1, str2 = input_
        assert answers[i] == solution(str1, str2)

if __name__ == '__main__':
    test()