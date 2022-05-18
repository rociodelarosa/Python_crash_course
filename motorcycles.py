# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

"""Agregar a una lista"""
# motorcycles.append('ducati')
# print(motorcycles)

"""Agregaren una posicion dada"""
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

"""Removiendo un item"""
# del motorcycles[1]
# print(motorcycles)

"""Remueve el último item pero deja trabajar con él luego de removerlo"""
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

"""Remuevo una posicion dada pero guardo el item con pop"""
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# print(motorcycles)

"""Remuevo buscando el item que quiero eliminar"""
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")