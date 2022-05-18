# Ejemplo 1
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# Ejemplo 2: el orden de los factores puede afectar el producto o no, si defino la variable al llamar la funcion
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('harry', 'hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# Ejemplo 3: valor por default
def describe_pet(pet_name, animal_type='dog'): # la variable indefinida va primero, al crear una variable con valor default no se deja espacio a os lados del =
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') # puedo cmabiar el valor de la variable con valor por default