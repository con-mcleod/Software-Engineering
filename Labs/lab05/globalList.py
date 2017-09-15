currList = []

def bubbleSort(array):

	global currList;

	exchanges = True
	passnum = len(array)-1


	while passnum > 0 and exchanges:

		currList.append(array[:])

		exchanges = False
		for i in range(passnum):


			if array[i]>array[i+1]:
				
				exchanges = True
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp


				


	return currList


array = [3,2,1]
bubbleSort(array)
print (currList)