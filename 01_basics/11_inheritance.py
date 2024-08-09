class Animal:
    def __init__(self,name): # Work as a contructor in python
        self.name=name      #self is like this in python
    
    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"


generic_animal=Animal("Generic")
dog=Dog("Buddy")

print(generic_animal.speak())
print(dog.speak())

another_animal=Animal("Someone")

print(another_animal.speak())