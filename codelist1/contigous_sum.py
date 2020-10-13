for _ in range(int(input())):
    N,S=list(int(x) for x in input().split(" "))
    arr=list(int(x) for x in input().split(" "))
    def sum_finder(arr,a,sum=0):
        for i in range(a,len(arr)):
            sum+=arr[i]
            if S==sum:
                print(a+1,i+1)
                return 1
        return 0
    def summ(arr):
        sum=0
        for i in range(0,len(arr)):
            if sum_finder(arr,i):
                break
    summ(arr)
