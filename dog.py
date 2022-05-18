class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        # metodo especial que python corre automaticamente al crear una nueva instancia
        # basada en la clase Dog().
        # Los __ al comienzo y al final son por convención y previene conflictos con 
        # otros nombres
        """Initialize name and age attributes."""
        self.name = name # cualquier variable con el prefijo self (como self.name) está oisponible para cada uno de los otros métodos en la clase. LAs variables que son acccesibles de esta forma se les llaman atributos
        self.age = age
    
    def sit(self):
        """Simulate a dog asitting in responde to a command."""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " roller over!")


my_dog = Dog('willie', 6) # que empiece con letra mayuscula normalmente refiere a una clase (Dog()), si empieza con minuscula refiere a una instancia de esa clase (my_dog())
# my_dog.sit()
# my_dog.roll_over()
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()