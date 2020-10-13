class father:
    def __init__(self):
        self.property=800000
    def display(self):
        print("Father propety=",self.property)
class son(father):
    def __init__(self):
        self.property=100000000
    def display1(self):
        print("Son property=",self.property)
s=son()
s.display()
s.display1()
         
     
