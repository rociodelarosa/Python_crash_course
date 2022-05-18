from audioop import reverse
from unittest import case


cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# cars.sort(reverse=True)
print(cars)

"""Ordenar pero mantener la lista original intacta"""
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

"""Cambia permanentemente la lista a su reversa"""
cars.reverse()
print(cars)

"""Vuelve a revertir la lista"""
cars.reverse()
print(cars)

print(len(cars))