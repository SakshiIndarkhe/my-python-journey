class Animal:
    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
mycat=Cat()
mydog=Dog()

print(mydog.speak())