from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

currList = []

@app.route('/', methods=["GET", "POST"])
def index():

	global currList

	if request.method == "POST":
		inputString = request.form["array"]

		myList = [int(x) for x in inputString.split(',') if x]

		exchanges = True
		passnum = len(myList)-1

		while passnum > 0 and exchanges:
			currList.append(myList[:])
			exchanges = False
			for i in range(passnum):

				if myList[i]>myList[i+1]:
					
					exchanges = True
					temp = myList[i]
					myList[i] = myList[i+1]
					myList[i+1] = temp

			currList.append(myList[:])
			
			passnum = passnum-1

		

		user_input.append(currList)

		return redirect(url_for('bubbleSort'))
	
	return render_template('index.html')

@app.route('/sorted')
def bubbleSort():

	return render_template('sorted.html', myList=user_input)