def fibonacci(n) :
	if n <= 1 :
		return n
	else :
		return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number for the fibonacci sequence: "))
print(fibonacci(n))