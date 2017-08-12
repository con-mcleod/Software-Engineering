inputString = input(str())

#make all words lower case
#inputString = inputString.lower()

#split the string up into words and store in an array
words = inputString.split()
#sort the words in the array alphabetically
words.sort()


def uniqueWords(words) :
	uniqueList = []
	for word in words:
		if word.lower() not in uniqueList:
			uniqueList.append(word) 
	return uniqueList

#create string of sorted, non-duplicate entries, list
uniqueWords = ' '.join(uniqueWords(words))

#print the list
print (uniqueWords)