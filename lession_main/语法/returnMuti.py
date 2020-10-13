#!/usr/bin/python
#coding:utf-8
import math

def quadratic_equation(a, b, c):
    x = b*b - 4*a*c
    if x < 0 :
        return none
    elif x == 0 :
        return -b / (2*a)
    else :
        nx = (math.sqrt(x) - b ) / (2*a)
        ny = (-math.sqrt(x) - b ) / (2*a)
        return nx , ny

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
