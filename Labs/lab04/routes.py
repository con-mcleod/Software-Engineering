from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		name = request.form["name"]
		zID = int(request.form["zID"])
		description = request.form["desc"]


		with open('example.csv','a') as csv_out:
			writer = csv.writer(csv_out)
			writer.writerow([name, zID, description])

		user_input.append([name, zID, description])
		
		return redirect(url_for('helloAll'))
	return render_template('index.html')

@app.route('/Hello')
def helloAll():

	with open('example.csv','r') as csv_in:
		reader = csv.reader(csv_in)
		for row in reader:
			user_input.append([row[0], row[1], row[2]])
			print(row)
			redirect(url_for('helloPerson', name=row[0], id=row[1], desc=row[2]))
			
	return render_template('Hello.html', all_users=user_input)

@app.route("/helloPage/<name>")
def helloPerson(name,id,desc):

	return render_template("helloPage.html", name=name, id=id, desc=desc)

#	with open('example.csv','r') as csv_in:
#		reader = csv.reader(csv_in)
#		for row in reader:
#			if name == row[0] :
#				return render_template("helloPage.html", name=row[0], id=row[1], desc=row[2])
#			else:
#				return 'Some response'
