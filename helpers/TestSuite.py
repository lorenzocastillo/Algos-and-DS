def Test(f):
    def g():
        print("\nTesting %s: " % f.__name__)
        f()
    return g


def Assert(expected, f, *args, verbose=True, descrip="", multiple_expected=False):
    if verbose:
        print('Testing: %s. args: %s' % (f.__name__, str(args)))
        if descrip:
            print('Description: %s' % descrip)
    res_f = f(*args)
    if multiple_expected:
        assert res_f == expected or res_f in expected, "Possible results %s, got %s" % (str(expected), str(res_f))
    else:
        assert res_f == expected, "Expected is %s, got %s" % (str(expected), str(res_f))
    if verbose:
        print('Success')



