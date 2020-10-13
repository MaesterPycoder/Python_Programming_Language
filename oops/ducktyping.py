class Duck:
    def talk(self):
        print("Quack! Quack!")
class Human:
    def talk(self):
        print("Hello Brother")
def call_talk(obj):
    obj.talk()
x=Duck()
y=Human()
call_talk(x)
call_talk(y)
