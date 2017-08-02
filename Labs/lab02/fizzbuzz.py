def fizzbuzz(n):
	count = 0
	while count < 101:
		if count % n == 0:
			msg = "FizzBuzz"
		else:
			msg = str(count)
		print (msg)
		count += 1

nvalue = int(input("Select a parameter for FizzBuzz: "))
fizzbuzz(nvalue)