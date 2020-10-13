n=int(input("Enter any number:"))
for i in range(2,n):
    if n==2:
        print("It's a prime number")
        break
    elif n%i!=0:
        print("it's prime number")
        break
