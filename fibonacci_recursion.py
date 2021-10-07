num = int(input())


def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci_list(x):
	for i in range(x):
		print(fibonacci(i))


fibonacci_list(num)
