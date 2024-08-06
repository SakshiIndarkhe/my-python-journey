a=10
b=20
c=a+b
print("Addition of a",a, "and b :",b ,"is",c)

# Below is using function

def Addition():
    iNo1,iNo2=234,654
    iAns=iNo1+iNo2
    print("Addition is",iAns)

Addition()

##################

def Addition2(iNo1:int,iNo2:int):
    iAns=iNo1+iNo2
    return iAns

Add=Addition2(12,33)
print("Addition of two number",Add)

#######################

def add_input(iNo1:int,iNo2:int):
    return iNo1+iNo2

print("Enter two number for Addition")
val_1=input()
val_2=input()

add_ans=add_input(val_1,val_2)

print("Addition of two number which you gave as input is",add_ans)