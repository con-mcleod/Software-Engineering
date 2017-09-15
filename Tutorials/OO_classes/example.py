class Course:
	#title, abstract, date, venue, attendees, trainer

	def __init__(self, title, abstract, date, venue, attendees, trainer):
		self.title = title
		self.abstract = abstract
		self.date = date
		self.venue = venue
		self.attendees = attendees
		self.trainer = trainer

	def addStudent(self, attendees):
		self.attendees.append(attendees)

	def __str__(self):
		return self.title + " " + self.abstract

	def __eq__(self, other):
		return self.title == other.title

Comp1531 = Course("Comp1531", "Software Engineering Fundamentals", "01/01/2017", "CSE", [], None)

Comp1531.addStudent("Student1")
print(Comp1531)