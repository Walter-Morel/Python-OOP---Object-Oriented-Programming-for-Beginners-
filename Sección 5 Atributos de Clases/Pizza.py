class Pizza:

    price = 12.99

    def __init__(self, description, toppings, crust):
        self.description = description
        self.toppings = toppings
        self.crust = crust


print(Pizza.price)

my_pizza = Pizza('Margherita', ['Basil', 'Mushrooms'], 'New York Style')
print(my_pizza.price)

#Modificamos la instancia colocando otro precio distinto
Pizza.price = 13.99
print(Pizza.price)
print(my_pizza.price)
        