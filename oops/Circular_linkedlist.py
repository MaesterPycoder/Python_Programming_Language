class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedLists:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
        cur=self.head
        new_node.next=cur
        while cur.next!=self.head:
            cur=cur.next
        cur.next=new_node
        self.head=new_node
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.head.next=self.head
            return
        cur=self.head
        while cur.next!=self.head:
            cur=cur.next
        cur.next=new_node
        new_node.next=self.head
    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
    def delete_last_node(self):
        if self.head==None:
            raise ValueError("List is Empty")
        cur=self.head
        prev=None
        while cur.next !=self.head:
            prev=cur
            cur=cur.next
        prev.next=self.head
        cur=None
    def delete_first_node(self):
        if self.head==None:
            raise ValueError("List is Empty")
        cur=self.head
        prev=None
        nxt=cur.next
        while cur.next !=self.head:
            prev=cur
            cur=cur.next
        cur.next=nxt
        self.head=nxt
    def remove_node_byData(self,key):
        cur=self.head
        prev=None
        if self.head==None:
            raise ValueError("list is Empty")
        if key==cur.data:
            return self.delete_first_node()
        while cur.next!=self.head:
            prev=cur
            cur=cur.next
            if cur.data==key:
                temp=cur
                prev.next=cur.next
                cur=cur.next
                temp.next=None
    def length_cllist(self):
        count=1
        cur=self.head
        while cur.next !=self.head:
            count+=1
            cur=cur.next
        return count
    def remove_node(self,node):
        cur=self.head
        prev=None
        if self.head==None:
            raise ValueError("list is Empty")
        if node==self.head:
            nxt=cur.next
            while cur.next !=self.head:
                prev=cur
                cur=cur.next
            cur.next=nxt
            self.head=nxt       
        while cur.next!=self.head:
            prev=cur
            cur=cur.next
            if cur==node:
                temp=cur
                prev.next=cur.next
                cur=cur.next
                temp.next=None
    def josephus_circle(self,step):
        cur=self.head
        l=cllist.length_cllist
        while l>1:
            count=1
            while count!=step:
                cur=cur.next
                count+=1
            print("Removed node:::",cur)
            self.remove_node(cur)
            cur=cur.next
            l=cllist.length_cllist
    def split_list(self,key):
        cllist1=CircularLinkedLists()
        cllist2=CircularLinkedLists()
        cur=self.head
        f=1
        while cur.next != self.head :
            if cur.data != key and f==1:
                cllist1.append(cur.data)
            if cur.data == key and f==1:
                cllist1.append(cur.data)
                f=0
            cur=cur.next
            if f==0:
                cllist2.append(cur.data)
        cllist1.print_list()
        print("And")
        cllist2.print_list()
cllist=CircularLinkedLists()
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.append("G")
cllist.prepend("B")
cllist.prepend("A")
#cllist.split_list("D")           
#print(cllist.length_cllist())
cllist.josephus_circle(2)      #Error
#cllist.remove_node_byData("D")
#cllist.delete_first_node()
#cllist.delete_last_node()
#cllist.print_list()
