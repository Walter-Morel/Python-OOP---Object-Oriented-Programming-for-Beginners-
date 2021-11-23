class   Quadruped:
    
    num_feet = 4

    def __init__(self, animals, breeds, predator, feet):
        self.animals = animals
        self.breeds = breeds
        self.predator = predator
        self.feet = []
        

animals_quadruped = Quadruped('Dog', 'Canine', 'none', Quadruped.num_feet)
print('Animals Quadruped is.')
print('Animals: {}'.format(animals_quadruped.animals))
print('Breeds: {}'.format(animals_quadruped.breeds))
print('Predator: {}'.format(animals_quadruped.predator))
print('Feet: {}'.format(animals_quadruped.num_feet))

        