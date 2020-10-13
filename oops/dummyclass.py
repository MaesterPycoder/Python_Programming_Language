class connection:
    verbose=0     #class variable
    def __init__(self,host):
        self.host=host     #instance variable
        self.avar=0
    def checkbug(self,val):
        self.avar=val
    def debug(self,y):
        connection.verbose+=20
        self.verbose=y     #class or instance variable
    def connect(self):
        if self.verbose:
            print("connnecting to",self.host)
        else:
            print("can't connect to",self.host)
con=connection("lenovo")
print("initial avar in con=",con.avar)
con.checkbug(77)
print("final avar in con=",con.avar)
print("verbose for con=",con.verbose)
con.debug(1)
con.debug(1)
con.debug(1)
con.connect()
print("                     ")

print("verbose value in class=",connection.verbose)
print("                             ")
kon=connection("Dell")
print("initial avar in kon=",kon.avar)
print("final avar in kon=",kon.avar)
print("verbose for kon=",kon.verbose)
kon.connect()