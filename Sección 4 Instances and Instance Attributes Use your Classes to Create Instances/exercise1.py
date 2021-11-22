class Dog:
    def __init__(self, age, name, is_male, weight):
        self.age = age
        self.name = name
        self.is_male = is_male
        self.weight = weight


my_dog = Dog(5, "Yogi", True, 15)
print(my_dog)