"""
# shortcut
@some_decorator
def some_function(arg):
    # blah blah

# No shortcut
def some_function(arg):
    # blah blah
some_function = some_decorator(some_function)
"""

def printlog(func):
    def wrapper(*arg, **kwargs): # use variable arguments
        print('CALLING: {}'.format(func.__name__))
        return func(*arg, **kwargs)
    return wrapper

@printlog
def foo(x):
    print(x + 2)

@printlog
def baz(x, y):
    print(x * y)



foo(9)
baz(3, 2)
