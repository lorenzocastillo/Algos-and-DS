
def sort_stacks(s1):
    s2 = []
    n = len(s1)
    while s2 != n and s1:

        temp = s1.pop(-1)

        while s2 and temp > s2[-1]:
            s1.append(s2.pop(-1))

        s2.append(temp)
    return s2

s1 = [5,4,3,2,1]
s1 = [1,2,3,4,5]
s1 = [4,2,1,5,3]
print(sort_stacks(s1))