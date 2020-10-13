def optimalCandies(n,arr):
    candies = [1]*n
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            candies[i+1] = candies[i]+1
    for i in range(n-1,0,-1):
        if arr[i-1]>arr[i] and candies[i-1]<=candies[i]:
            candies[i-1] = candies[i]+1
    return sum(candies)
for _ in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().strip().split()]
  print(optimalCandies(n,arr))