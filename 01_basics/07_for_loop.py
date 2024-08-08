name="Sakshi"
for x in name:
    print(x)

##################
for x in range(1,10):
    print(x)

################
print("Generate tables")
print("Enter the number you want to generate the tables")
iNo=int(input())
for x in range(1,11):
    iAns=x*iNo
    print(iAns)

##############
thislist=["apple","cherry","mango","kiwi"]
for x in thislist:
    print(x)  #if print(thislist) is added then list will be print four times
    if "apple" in x:
        print("Apple is present")

############################
#Summation of numbers
print("Enter the number for summation")
val=int(input())
sum=0
for i in range(1,val+1):
    sum+=i

print(sum)
