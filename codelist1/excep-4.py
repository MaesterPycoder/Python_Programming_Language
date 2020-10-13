try:
    x=int(input("Enter a number:"))
    assert x>=5 and x<=10
    print("you entered correct")
except AssertionError:
    print("condition is not fullfilled")
