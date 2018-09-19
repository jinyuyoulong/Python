
def for1():
	arr = ['one','two','three']
	for item in arr:
		print(item)

def for_range():
	for x in range(1,10):
		print(x)

def while1():
	num = 0
	n = 99
	while n > 0:
		num = num+n
		n=n-2

	print(num)

def main():
	# for1()
	# for_range()
	while1()

if __name__ == '__main__':
	main()