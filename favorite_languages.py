# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python', # se recomienda dejar coma (,) al final como estandar, también es útil por si es necesario agregar mas claves y valores al diccionario
# }

# print("Sarah's favorite language is " + 
#     favorite_languages['sarah'].title() +
#     ".")

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + 
#         language.title() +
#         ".")

# print("The following languages has been mentioned:")
# for language in set(favorite_languages.values()): #set es similar a un listado pero solo nos entrega los valores unicos
#     print(language.title())

# Ejercicio librerías estandar
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "
        + language.title()  + ".")