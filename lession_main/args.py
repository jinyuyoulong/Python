import math
def average(*args):
    if len(args)==0:
        return 0.0
    else:
        return sum(args)*1.0/len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)