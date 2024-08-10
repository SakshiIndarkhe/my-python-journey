person=["Sakshi","Chaitanya","RUpali","Arya","Prerna"]

for i in person:
    print(i)

if "Sakshi" in person:
    print("Sakshi is in the list")

print("Lenght of list is",len(person))

#Creating list using list() constructor
age=list((12,23,44,55,33))
print(age[0])
print(age[-1])

print(person[2:5])
person[1]="Lovely"
print(person[1])

person.insert(2,"kajol")
print(person)

person.append("lily")
print(person)

person.remove("lily")
print(person)


