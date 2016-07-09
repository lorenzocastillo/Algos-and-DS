def Test(f):
    def g():
        print("\nTesting %s: " % f.__name__)
        f()
    return g


def Assert(expected, f, *args, verbose=True, descrip=""):
    if verbose:
        print('Testing: %s. args: %s' % (f.__name__, str(args)))
        if descrip:
            print('Description: %s' % descrip)
    res_f = f(*args)
    assert res_f == expected , "Expected is %s, got %s" % (str(expected), str(res_f))
    if verbose:
        print('Success')