print("Welcome to PYBank version 0.0.1")

class Bankaccount:
    
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance

    def deposite(self,newamount):
        
        self.balance=newamount+self.balance

        return self.balance

    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.balance: return False
        self.balance=self.balance-withdraw_amount

        return self.balance

    def checkbalance(self):
        return self.balance
    
class SavingAccount(Bankaccount):
    def Intreset(self):
        intreset=(self.balance*1*3)//100
        return intreset

    
myacc=SavingAccount(123,3000)

print("Current Balance",myacc.checkbalance())
newbalance=myacc.deposite(1000)

print("After depositing",newbalance)

afterwithdraw=myacc.withdraw(2000)
print("Balance after withdrawing",afterwithdraw)

new =myacc.checkbalance()

print("Current Balance",new)

myintrest=myacc.Intreset()
print("Intreset on Current balance",myintrest)