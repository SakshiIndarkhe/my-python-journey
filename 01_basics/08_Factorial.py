#Factorial for 10 - 10*9*8...*1

print("Enter the number for Factorial")
val=int(input())
iFact=1
for i in range(1,val+1):
    iFact*=i

print("Factorial of",val,"is",iFact)