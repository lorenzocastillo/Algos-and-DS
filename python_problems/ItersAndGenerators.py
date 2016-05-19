class reverse_iter:
    def __init__(self, xs):
        self.i = len(xs)
        self.xs = xs
    def __iter__(self):
        return self
    def __next__(self):
        while self.i > 0:
            self.i = self.i - 1
            return self.xs[self.i]
        raise StopIteration()

my_iter = reverse_iter([1,2,3])
next(my_iter)
print(list(my_iter))
