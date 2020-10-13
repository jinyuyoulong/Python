#!/usr/bin/python
#coding: utf8
# def f():
#     print 'call f()...'
#     def g():
#         print 'call g()...'
#     return g

# x = f()
# print x
# x()

# 延时计算
# def calc_sum(lst):
#     def lazy_sum():
#         return sum(lst)
#     return lazy_sum

# 调用calc_sum()并没有计算出结果，而是返回函数:
# f = calc_sum([1, 2, 3, 4])
# print f
# 对返回的函数进行调用时，才计算出结果:
# print f()

def calc_prod(lst):
	def lazy_prod():
		def prod(x,y):
			return x*y
		return reduce(prod,lst)
	return lazy_prod
    

f = calc_prod([1, 2, 3, 4])
print f()