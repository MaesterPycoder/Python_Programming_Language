class Heap:
    def __init__(self):
        self.heapList = list()
        self.size = 0
    #indexing the nodes
    def leftChild(self, i):
        return 2*i+1
    def rightChild(self, i):
        return 2*i+2
    def parent(self, i):
        return i//2
    # Getting MAX in MaxHeap and MIN Values in MinHeap
    def getMax(self):# for MaxHeap: O(1) 
        if self.size > 0:
            return self.heapList[0]
        else:raise Exception("Empty Heap")
    def getMin(self): # for MinHeap: O(1)
        if self.size > 0:
            return self.heapList[0]
        else:raise Exception("Empty Heap")
    #Heapifying the complete Binary tree
    def percolateDown(self, i):
        while (i*2)<= self.size:
            minimumChild = self.minChild(i)
            if self.heapList[i]>self.heapList[minimumChild]:
                self.heapList[i],self.heapList[minimumChild]=self.heapList[minimumChild],self.heapList[i]
            i=minimumChild
    def minChild(self, i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    def percolateUp(self, i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2]=self.heapList[i//2],self.heapList[i]
            i=i//2
    # Inserting the elements
    def insert(self, val):
        self.heapList.append(val)
        self.size+=1
        self.percolateUp(self.size-1)
    # Deleting the elements
    def delete(self):
        pass
    def printHeap(self):
        for ele in self.heapList:
            print(ele,end=" ")
hp=Heap()
hp.insert(10)
hp.insert(20)
hp.insert(30)
hp.insert(40)
hp.insert(50)
hp.insert(60)
hp.insert(70)
hp.printHeap()