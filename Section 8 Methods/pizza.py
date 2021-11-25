#metodo de cadena
class Pizza:
 
    def __init__(self):
        self.toppings = []
 
    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self
 
    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())


pizza = Pizza()            
'''Esta es la forma tradicional de acceder a un metodo
pizza.add_topping('mushrooms').add_topping('olives').add_topping('chikens').display_toppings()
print(pizza)'''

#para encadenar un metodo y que el codigo sea mas legible lo hacemos de la siguiente forma
pizza.add_topping('mushrooms')\
    .add_topping('olives')\
    .add_topping('pepino')\
    .add_topping('chickens')\
    .display_toppings()
#se agrega \ despues de un argumento