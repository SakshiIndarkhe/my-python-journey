#map
numbers=[1,2,3,4,5]
def addition(n):
    return n+n

iAns=map(addition,numbers)

print(list(iAns))

#map() with lambda function

numbers=[1,2,3,4,5,6,7,8,9]

Ans=map(lambda x:x**2,numbers)

print(list(Ans))

#filter()

number=[1,2,3,4,5,6,7,8,9]

fun=filter(lambda x:x%2==0,numbers)

print(list(fun))