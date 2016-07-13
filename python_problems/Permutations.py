from collections import Counter

def distribute(a, lst):
    result = list()
    for elem in lst:
        for i in range(len(elem) + 1):
            result.append(elem[:i] + a + elem[i:])
    return result


def permutations(string):
    def permute(s, i):
        if i == len(s):
            return ['']
        else:
            return distribute(s[i],permute(s, i + 1))
    return permute(string, 0)


def permutations_nodups(string):
    counter = Counter(string)
    result = list()

    def perms(prefix, remaining):
        if remaining == 0:
            result.append(prefix)
        else:
            for key, count in counter.items():
                if count > 0:
                    counter[key] -= 1
                    perms(prefix + key, remaining - 1)
                    counter[key] = count

    perms("",len(string))
    return result

print(permutations_nodups('abc'))

def parens(n):
    def insert(string):
        res = list()
        for i in range(len(string) + 1):
            for j in range(i,len(string) + 1):
                res.append(string[:i] + "(" + string[i:j] + ")" + string[j:])
        return res
    if n == 0:
        return [""]
    else:
        ## return sum(map(insert, parens(n-2)), list()) MAP-REDUCE VERSION
        xs = list()
        for s in parens(n-2):
            xs += insert(s)
        return xs



