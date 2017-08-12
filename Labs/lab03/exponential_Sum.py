def exponential_Sum(n) :

	counter = n
	answer = 0

	while (counter >= 0) :
		answer += n**(counter)
		counter = counter - 1
	return answer

nValue = int(input("Enter a value: "))

print (exponential_Sum(nValue))