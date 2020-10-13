class Dog:
    def Bark(self):
        print("Bow! Bow!")
class Duck:
    def talk(self):
        print("Quack! Quack!")
class Human:
    def talk(self):
        print("Hello Brother!")
def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"Bark"):
        obj.Bark()
    else:
        print("Wrong attribute passed")
x=Duck()
call_talk(x)
y=Human()
call_talk(y)
z=Dog()
call_talk(z)
