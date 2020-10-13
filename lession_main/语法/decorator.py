#!/usr/bin/python
#-*- coding:utf-8 -*-

# 装饰者 装饰化器
# 简言之，python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。
# 一般而言，我们要想拓展原来函数代码，最直接的办法就是侵入代码里面修改，

def f1(x):
    print "log"
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