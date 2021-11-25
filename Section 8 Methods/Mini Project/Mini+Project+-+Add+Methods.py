class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                        "Talina": [28, "555-765-452", ["Cello"]],
                        "Eric":   [12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	def print_students_data(self):
		for name in MusicSchool.students:
			self.print_student(name)

	def print_student(self, name):
		data = MusicSchool.students[name]
		print('Student: '+ name +' who is ' + str(data[0]) + ' year old and is taking ' + str(data[2]))

	def add_student(self, name, data):
            MusicSchool.students[name] = data



# Create the instance
school_data = MusicSchool(8, 15000)
school_data.print_students_data()
school_data.print_student('Gino')
school_data.add_student('Ana', [30, '22344312', ['piano']])
print(school_data.print_students_data())



# Call the methods
