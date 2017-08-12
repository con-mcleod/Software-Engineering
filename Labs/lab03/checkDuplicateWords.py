inputString = input(str("Enter the string to check for duplicates: "))
words = inputString.split()

def checkDuplicate(words) :
	uniqueWords = []
	for word in words :
		if word in uniqueWords :
			print (False)
			return
		else :
			[uniqueWords.append(word)]
			continue
	print (True)
	return 
	
checkDuplicate(words)