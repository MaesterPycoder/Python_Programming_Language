import sys
def findMinDiff(arr, n, m): 
	if (m==0 or n==0): 
		return 0
	arr.sort() 
	if (n < m): 
		return -1
	min_diff = sys.maxsize 
	i=0
	while(i+m-1<n ): 
		diff = arr[i+m-1] - arr[i] 
		if (diff < min_diff): 
			min_diff = diff 
		i+=1
		
	return min_diff 

if __name__ == "__main__": 
	arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50] 
	m = 7 
	n = len(arr) 
	print("Minimum difference is", findMinDiff(arr, n, m)) 
	

