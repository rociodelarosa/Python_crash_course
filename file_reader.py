# Ejercicio 1
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


# Ejercicio 2
# FILENAME = 'pi_digits.txt' # PEP8, constantes en mayusculas

# with open(FILENAME) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# Ejercicio 3
FILENAME = 'pi_digits.txt'

with open(FILENAME) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())