from flask import Flask, redirect, render_template, request, url_for
from server import app
from math import sin, cos, tan, log, sqrt


expr = ""

@app.route('/', methods=["GET", "POST"])
def index():
	global expr

	if request.method == "POST":
		keyPressed = request.form['bt']
		
		if keyPressed == "C":
			expr = expr[:-1]

		elif keyPressed == "CE":
			expr = ""

		elif keyPressed == "=":
			expr = str(eval(expr))
			return render_template('index.html', expr=expr)

		else:
			expr = expr + str(keyPressed)

		return render_template('index.html', expr=expr)


	return render_template('index.html', expr=expr)