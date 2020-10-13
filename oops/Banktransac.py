import sys
class Bank:
    def __init__(self,name,curr_Bal=0):
        self.name=name
        self.curr_Bal=curr_Bal
    def deposit(self,amount):
        self.curr_Bal+=amount
        return self.curr_Bal
    def  withdraw(self,amount):
        if self.curr_Bal>amount:
            self.curr_Bal=self.curr_Bal-amount
            return self.curr_Bal
        else:
            print("Insufficient Balance.Transaction cannot be proceed")
#create an account
name=input("Enter name of the customer:")
b=Bank(name)
#Repeat the process till the choice is exit or Enter
while(True):
    print("options available:\n")
    print("d-Deposit \n w-Withdraw \n e-exit")
    choice=input("Enter your choice of transaction:")
    if choice=="e" or choice=="E":
        print("Thanks for using our service. Please visit again")
        sys.exit()
    amount=float(input("Enter amount:"))
    if choice=="d" or choice=="D":
        print("Balance after Deposit:",b.deposit(amount))
    if choice =="w" or choice=="W":
        print("Balance after withdrawal:",b.withdraw(amount))
    
