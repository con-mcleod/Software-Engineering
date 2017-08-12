fruitArray = ["apple", "pear", "orange"]

for i in range(len(fruitArray)) :
	if (fruitArray[i] != "pear") :
		print ('Current fruit is:', fruitArray[i])
	else :
		print ("Nice try, pear")

fruitArray.append("lemon")

print("Items in set: ")
for i in fruitArray:
	print(i)
print("----------")
print("# items in set:", len(fruitArray))