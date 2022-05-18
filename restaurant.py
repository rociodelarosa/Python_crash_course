class Restaurant():
    """Information about a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant"""
        print("The name of the restaurant is " + self.restaurant_name.title() + " and they have a type of " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        print("The restaurant is open")

restaurant = Restaurant("Cocina Peruana", "Peruvian")
restaurant.describe_restaurant()
restaurant.open_restaurant()