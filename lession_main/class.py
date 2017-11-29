class Student(object):
	"""test class"""
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.name = name
		self.score = score
	def print_score(self):
		print '%s: %s' % (self.name, self.score)
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
dart = Student('fans',98)
print dart.name
print dart.score
dart.print_score()
print dart.get_grade()