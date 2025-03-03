# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute
        print("vv")

    def speak(self):
        print("ani")
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
        def speak(self):
            print("Dog")
            return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
