class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queues:
    def __init__(self,limit):
        self.limit=limit
        self.front=None 
        self.rear=None
        self.size=0
    def print_Queue(self):
        if self.front is None:
            return
        cur=self.front
        while True:
            print(cur.data)
            if cur is self.rear:
                break
            cur=cur.next
    def enqueue(self,item):
        if self.size>=self.limit:
            raise  ValueError("Limit of data in queue is exceeded")
        new_node=Node(item)
        if self.front is None:
            self.front=self.rear=new_node
        else:
            cur=self.front
            while cur != self.rear:
                cur=cur.next
            cur.next=new_node
            self.rear=new_node
        self.size+=1
        return
    def dequeue(self):
        if self.size==0:
            raise ValueError("Dequeuing on empty list cannot be done")
        if self.size==1:
            self.front=None 
            self.rear=None 
        else:
            cur=self.front
            self.front=cur.next
            cur=None
        self.size-=1
        return
    def size_of_Queue(self):
        return self.size
q=Queues(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print("size of queue=",q.size_of_Queue())
q.print_Queue()