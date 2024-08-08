#Program to show Factors and Non Factors and checking Perfect number

print("Enter the Number")
iVal=int(input())

for i in range(1,iVal+1):
    if(iVal%i==0):
        print(i)

for i in range(1,iVal+1):
    if(iVal%i!=0):
        print("Non Factors are",i)
Sumdivisor=0
for i in range(1,iVal//2+1):
    if(iVal%i==0):
        Sumdivisor+=i
if(Sumdivisor==iVal):
    print("Number is perfect")
else:
    print("Number is not perfect")
    
