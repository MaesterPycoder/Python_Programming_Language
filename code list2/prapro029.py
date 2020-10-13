import numpy as np
ar=list(int(x) for x in input("Enter space separated elements:").split(" "))
arr=np.array(ar)
lst=np.reshape(arr,(4,4))
print(lst)
