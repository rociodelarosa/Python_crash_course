FILENAME = 'programming.txt'

# Ejercicio 1
# with open(FILENAME, 'w') as file_object:
    # file_object.write("I love programming.\n")
    # file_object.write("I love creating new games.\n")

# Ejercicio 2
with open(FILENAME, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    