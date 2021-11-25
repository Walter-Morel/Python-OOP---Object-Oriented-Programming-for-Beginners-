class Calculator:
 
	def add(self, a, b):
		print(a + b)
 
	def multiply(self, a, b):
		return a * b


my_calculator = Calculator()
my_calculator.add(5, 6)
print(my_calculator.add(5, 6))

my_calculator.multiply(5, 6)
print(my_calculator.multiply(5, 6))