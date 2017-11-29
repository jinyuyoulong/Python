# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def g(j):
            def f():
                return j*j
            return f
        r = g(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()