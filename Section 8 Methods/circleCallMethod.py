class Circle:
    
    pi = 3.1416
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    # Add the method below this line
    def find_area(self):
        return Circle.pi * (self.radius) ** 2


        
blue_circle = Circle(15, "Blue")
final_area = blue_circle.find_area()
print(final_area)
