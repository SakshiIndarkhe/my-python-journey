def divisiblebyfive(iNo):
    if (iNo%5==0):
        return True
    else:
        return False

def divi_by_3and5(iNo):
    if ((iNo%5==0) &(iNo%3==0)):
        return True
    else:
        return False

def divi_by_3or5(iNo):
    if ((iNo%5==0)|(iNo%3==0)):
        return True
    else:
        return False 

print("Enter the number")
val=int(input()) # type casting

bAns=divisiblebyfive(val)
bbAns=divi_by_3and5(val)
bbbAns=divi_by_3or5(val)
if (bAns==True):
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

if (bbAns==True):
    print("Number is divisible by 5 and 3")
else:
    print("Number is not divisible by 5 and 3")

if (bAns==True):
    print("Number is divisible by 5 or 3")
else:
    print("Number is not divisible by 5 or 3")