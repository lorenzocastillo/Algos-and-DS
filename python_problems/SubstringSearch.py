def rabin_karp(text, pattern):

    R = 256 # Size of the radix
    Q = 997 # a big prime number
    M = len(pattern)
    RM = 1 # R^(M-1) % Q
    for i in range(1, M):
        RM = (R * RM) % Q

    def hash(string, start, end):
        h = 0
        for i in range(start, end):
            c = string[i]
            h = (R*h + ord(c)) % Q
        return h

    def is_sub_same(end):
        """
        Checks if a pattern is equal to text ending at end
        :param end: the end index of the substring of text
        :return:
        """
        same = True
        for j in reversed(range(0, M)):
            if pattern[j] != text[end]:
                same = False
                break
            end -= 1
        return same

    pattern_hash = hash(pattern, 0, M)

    text_hash = hash(text, 0, M)

    if pattern_hash == text_hash:
        return 0

    for i in range(M, len(text)):
        text_hash = (text_hash + Q - RM * ord(text[i-M]) % Q) % Q
        text_hash = (text_hash * R + ord(text[i])) % Q
        if text_hash == pattern_hash:
            if is_sub_same(i):
                return i - M + 1

    return -1


def boyer_moore(text, pattern):
    N = len(text)
    M = len(pattern)

    def generate_offsets():
        right = {t: -1 for t in text}

        for j, p in enumerate(pattern):
            if p not in right:
                return -1
            right[p] = j
        return right

    offsets = generate_offsets()

    i = 0
    while i < (N - M + 1):
        skip = 0
        for j in reversed(range(0, M)):
            if pattern[j] != text[i + j]:
                skip = max(1, j - offsets[text[i+j]])
                break
        if skip == 0:
            return i
        i += skip
    return -1

# print(rabin_karp('Xsum lists', 'sum'))
print(boyer_moore('XxxsumsXlists', 'sums'))