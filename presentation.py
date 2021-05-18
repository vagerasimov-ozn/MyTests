def foo(x, y=0, z=0):
    return 100*x + 10*y + 1*z


def bar(*args, named_parameter="bar", lolly='fff'):   # add * for any number of parameters
    for arg in args:
        print(lolly, named_parameter, 'arg = ', arg)


bar(1, 2, 3)
bar(["jelly", "fish"])
bar("jelly", "fish", lolly='SEPARATOR')

'''print(foo(1, 2, 3))
print(foo(z=1, y=2, x=3))  # named parameters
print(foo(7))'''
