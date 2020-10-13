#!/usr/local/homebrew/bin/python3

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('2015-3-25')


# 三层嵌套 now = log('execute')(now)
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print('2015-3-25')

now()