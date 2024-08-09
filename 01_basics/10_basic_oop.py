class MyDoy:
    name="Pumpkin"

    def Sound(self):
        Breed="India"
        Age=4
        print(Breed)
        print(Age)

dogobj=MyDoy()
print(dogobj.name)
dogobj.Sound()

################

print("\n")
print("This is another example")

class sun:
    name="sakshi"
    age=21

    def personal(self):
        qualifi="BE Computer"
        marks=70.90

        print("Sakshi has complted her",qualifi,"with",marks,"marks")

class mun:
    name="Chaitanya"
    age=17

    def personal(self):
        qualifi="11th Commerce"
        marks=90

        print("Chaitnya is studing in class", qualifi,"and has secured ",marks,"last year")

sakshi=sun()
chaitanya=mun()

print(sakshi.name)
print(sakshi.age)

print(chaitanya.name)
print(chaitanya.age)

sakshi.personal()
chaitanya.personal()

####################################

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def bark(self):
        return f"{self.name} says Woof!!"
    
my_dog=Dog("Buddy",3)

print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())
