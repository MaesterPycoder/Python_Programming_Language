def optimalCandies(arr):
    n = len(arr)
    candies = [1]*n
    for i in range(n-1):            # Forward Looping
        if arr[i+1]>arr[i]:
            candies[i+1] = candies[i]+1

    for i in range(n-1,0,-1):       # Backward Looping
        if arr[i-1]>arr[i] and candies[i-1]<=candies[i]:
            candies[i-1] = candies[i]+1
    return sum(candies)

arr = [1,5,4,3,1,2]
print("Required Candies:",optimalCandies(arr))


# for _ in range(int(input("Enter no. of testcases:"))):
#   n = int(input("Array size:"))
#   print("Enter elements in space separated:")
#   arr = [int(x) for x in input().strip().split()]
#   print(optimalCandies(n,arr))