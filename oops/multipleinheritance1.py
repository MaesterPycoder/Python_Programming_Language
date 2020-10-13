class Father:
    def height(self):
        print("Height is 6 Feet")
class Mother:
    def color(self):
        print("Color is white")
class Child(Father,Mother):
    pass
c=Child()
print("Childs Inherited Qualities:")
c.height()
c.color()
