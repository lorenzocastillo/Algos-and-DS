import random

#random.seed(0)


def zero_or_one():
    return random.randrange(0,2)

def get_iterable(t=list, size=10, negative=False, min_num=0, max_num=50):
    if t == list:
        return get_list(size, negative, min_num, max_num)


def get_list(size, negative, min_num, max_num):
    if not negative:
        return [random.randint(min_num,max_num) for _ in range(size)]
    else:
        negative_one = -1
        return [(negative_one ** zero_or_one()) * random.randint(min_num,max_num) for _ in range(size)]
