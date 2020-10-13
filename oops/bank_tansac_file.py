#import datetime
import time
import sys
class Bank(object):
    def __init__(self,name,Bal=0):
        self.name=name
        self.Bal=Bal
        f.write("\n")
        f.write("Current Balnce="+str(self.Bal))
        f.write("\n")
    def deposit(self,amount):
        self.Bal+=amount
        f.write("Balance after Deposit:"+str(self.Bal)+"\n")
        return self.Bal
    def  withdraw(self,amount):
        if self.Bal>amount:
            self.Bal-=amount
            f.write("Balance after withdrawal:"+str(self.Bal)+"\n")
            return self.Bal
        else:
            print("SORRY! \n "+"Insufficient Balance.Transaction cannot be proceed")
            f.write("SORRY! \n "+"Insufficient Balance.Transaction cannot be proceed")
            f.write("\n")
#create an account
f=open("Mytransac.txt","a")
name=input("Enter name of the customer:")
f.write("Enter name of the customer:"+name)
f.write("\n")
b=Bank(name)
#Repeat the process till the choice is exit or Enter
while(True):
    f=open("Mytransac.txt","a")
    #now=datetime.datetime.now()
    now=time.ctime()
    print(now)
    f.write("Date & Time of Transaction::"+str(now))
    f.write("\n")
    print("options available:\n")
    f.write("options available:")
    f.write("\n")
    print("d or D-Deposit \n w or W-Withdraw \n e or E-exit")
    choice=None
    while(choice==None):
        choice=input("Enter your choice of transaction:")
        continue
    if choice=="e" or choice=="E":
        print("Transaction completed. Thanks and visit again")
        f.write("Transaction completed. Thanks and visit again \n")
        sys.exit()
    amount=float(input("Enter amount:"))
    f.write("amount entered="+str(amount))
    if choice=="d" or choice=="D":
        f.write("\n")
        f.write("Mode of transaction:Deposit")
        f.write("\n")
        print("Balance after Deposit:",b.deposit(amount))
    if choice =="w" or choice=="W":
        f.write("\n")
        f.write("Mode of transaction:Withdawal")
        f.write("\n")
        print("Balance after withdrawal:",b.withdraw(amount))
    print("------------------------------------------------------------------------------------------------------------")
    f.write("----------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.close()
