#list comprehension

square=[]

for x in range(1,6):
    square.append(x**2)

print(square)

#by using list comprehension

new_square=[x**2 for x in range(1,6)]

print(new_square)

#Even number

even=[]

for x in range (1,11):
    if (x%2==0):
        even.append(x)

print(even)

#list comprehension for above program

evens=[x for x in range(1,11) if (x%2==0)]

print(evens)

#even squared

even_square=[]

for x in range(1,11):
    if (x%2==0):
        even_square.append(x**2)

print(even_square)

#list comprehension

evensquared=[x**2 for x in range(1,11)if (x%2==0)]

print(evensquared)
