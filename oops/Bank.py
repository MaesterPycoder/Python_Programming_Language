import sys
class Bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return self.balance
        else:
            print("TRansaction cannot Proceed")
name=input("Enter name:")
b=Bank(name)
while(True):
    print("d-deposit \n w-withdrawal \n e-exit \n")
    choice=input("Enter choice=")
    amount=float(input("Enter amount="))
    if choice=="e" or choice=="E":
        print("thanks ! ,Visit agaiin")
        sys.exit()
    elif choice=="d" or choice=="D":
        print("Bakance after deposit=",b.deposit(amount))
    elif choice=="w" or choice=="W":
        print("Balance after withdrawal=",b.withdraw(amount))
    
    
        
