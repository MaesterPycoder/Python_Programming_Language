class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class priority_queue:
    def __init__(self,size):
        self.size=size
        self.length=0
        self.head=None
    def insert_into_pq(self,item,key):
        if self.length>=self.size:
            raise ValueError("OverFlow Occurred")
        assert key>0,"Entered Invalid Key"
        new_node=Node(item)
        if self.head is None:
            self.head=new_node
            self.length+=1
            return
        pos=0
        cur=self.head
        if key==1 and cur.next:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
            return
        while(pos<key-2 and cur.next):
            pos+=1
            cur=cur.next
        var=cur.next
        cur.next=new_node
        new_node.next=var
        self.length+=1
    def pop_item(self):
        if self.head is None:
            raise ValueError("UnderFlow Occurred")
        cur=self.head
        var=cur.data
        if self.length==1:
            self.head=None 
            self.length=0
            return var
        self.head=cur.next
        cur=None
        self.length-=1
        return var
    def print_pq(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def size_pq(self):
        return self.length
pq=priority_queue(15)
pq.insert_into_pq(1,1)
pq.insert_into_pq(2,2)
pq.insert_into_pq(3,3)
pq.insert_into_pq("a",1)
pq.insert_into_pq("b",2)
pq.insert_into_pq("O",9)
pq.insert_into_pq("e",5)
pq.insert_into_pq("p",10)
#print("poped item:",pq.pop_item())
print("items in list:")
pq.print_pq()