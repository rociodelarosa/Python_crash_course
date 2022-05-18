# Ejemplo 1
# pizzas = ['pepperoni', 'margarita', 'hawaiana']
# for pizza in pizzas:
#     print("I like " + pizza + " pizza")

# print("I really love pizza!")

# Ejemplo 2
# def make_pizza(*toppings): # *toppings genera una tupla, recibe cualquier dato y cantidad de datos que se le entregue y lo guarda dentro de una tupla
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('pepperoni', 'green peppers', 'extra cheese')

# Ejemplo 3
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('pepperoni', 'green peppers', 'extra cheese')


# Ejemplo 4
def make_pizza(size, *toppings): # *toppings siempre debe ir al final
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')