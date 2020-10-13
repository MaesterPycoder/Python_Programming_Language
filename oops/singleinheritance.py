class Bank(object):
    cash=100000
    @classmethod
    def available(cls):
        print("cash in Bank=",cls.cash)
class AndhraBank(Bank):
    pass
class StateBank(Bank):
    cash=200000
    @classmethod
    def available(cls):
        print("Total cash in Both the Banks=",cls.cash+Bank.cash)
a=AndhraBank()
a.available()
s=StateBank()
s.available()
