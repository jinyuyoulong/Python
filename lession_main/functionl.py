import math

if __name__ == '__main__':
	main()

def main():
	print(add(25, 9, math.sqrt))
	
def add(x, y, f):
    return f(x) + f(y)

