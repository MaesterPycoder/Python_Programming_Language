# worst case time complexity = O(n2)
# Best case time complexity(i.e,pivot is always middle of array) = O(nlogn)
# Space Complexity is O(logn) for best case and O(n) for worst case


def partition(A,l,h):
    pivot=A[h]
    i=l-1
    j=h
    while(i<j):
        while A[i]<=pivot:
            i+=1
        while A[i]>=pivot:
            j-=1
        if i<j:
            A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    return j
def quicksort(A,l,h):
    if l<h:
        pt=partition(A,l,h)
        quicksort(A,l,pt-1)
        quicksort(A,pt+1,h)
if __name__=='__main__':
    print("Enter elements of the array:")
    A=list(int(x) for x in input().split(" "))
    print("Initially:",A)
    quicksort(A,0,len(A)-1)
    print("Finally:",A)
   
    
    
        
