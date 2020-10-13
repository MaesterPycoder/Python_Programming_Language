try:
    class Duck:
        def talk(self):
            print("Quack! Quack!")
    class Human:
        def talk(self):
            print("Hello Brother")
    class dog:
        def bark(self):
            print("BOW! BOW!")
    def call_talk(obj):
        obj.talk()
    x=Duck()
    y=Human()
    call_talk(x)
    call_talk(y)
    z=dog()
    call_talk(z)
except AttributeError as m:
    print("Error occured ")
    print("Dog has no attribute talk but has Bark")
finally:
    print("Code executed")
    print("------------------------------")
