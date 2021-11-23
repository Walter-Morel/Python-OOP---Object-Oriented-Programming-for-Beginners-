class Spider:
    
    num_legs = 8
    num_eyes = 8
    
    def __init__(self, name, age, code, species):
        self.name = name
        self.age = age
        self.code = code
        self.species = species


Spider.num_legs = 5
Spider.num_eyes = 6
print(Spider.num_legs)
print(Spider.num_eyes)