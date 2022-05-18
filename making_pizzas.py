# Ejemplo 1
# import pizzas

# pizzas.make_pizza(16, 'pepperoni')
# pizzas.make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

# Ejemplo 2
# import pizzas as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

# Ejemplo 3
# from pizzas import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')

# Ejemplo 4
from pizzas import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'pepperoni', 'green peppers', 'extra cheese')

# Ejemplo 5
# from pizzas import * # trae todo, no se recomienda, puede sobreescribir funciones

# mp(16, 'pepperoni')
# mp(12, 'pepperoni', 'green peppers', 'extra cheese')