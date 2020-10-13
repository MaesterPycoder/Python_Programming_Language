n=int(input("Enter size of array:"))
a=list(int(x) for x in input("Enter elements:").split())
for i in range(n):
    if(a.count(a[i])>n/2):
        print(str(a[i])+", This is majority element")
        break
else:
    print("No Majority Element Found")
