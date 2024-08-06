#This is my first small project in Python

## Calulator using python ##
##version 0.1

print("Welcome to PyCal") #Name of Calculator

print("Enter two oprands")
iNo1=int(input())
iNo2=int(input())

print(" Two number Entered are",iNo1,"and",iNo2)

print ("Select the operation perform on this numbers")
print("1 for Addition")
print("2 for Substraction")
print("3 for Multiplication")
print("4 for Substraction")
op_num=int(input())
def Operations(iNo1:int,iNo2:int,op_num:int):
    if (op_num==1): return iNo1+iNo2
    elif (op_num==2): return iNo1-iNo2
    elif (op_num==3): return iNo1*iNo2
    elif (op_num==4): return iNo1//iNo2
    else : print("please enter valid number")

iAns=Operations(iNo1,iNo2,op_num)
print("Answer",iAns)

  

