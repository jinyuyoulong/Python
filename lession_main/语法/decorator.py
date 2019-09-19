# 装饰者 装饰化器

def f1(x):
    pass
print f1.__name__

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__



def performance(unit):
    def f1(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            return f(*args,**kw)
        return wrapper
    return f1

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__