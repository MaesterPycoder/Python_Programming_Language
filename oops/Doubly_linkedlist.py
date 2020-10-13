class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedLists:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.prev=None
            self.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            new_node.prev=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.prev=None
            self.head=new_node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None
    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
    def add_after_node(self,key,data):
        cur=self.head
        while cur:
            if cur.next is None and cur.data==key:
                self.append(data)
                return
            elif(cur.data==key):
                new_node=Node(data)
                nxt=cur.next
                cur.next=new_node
                new_node.next=nxt
                new_node.prev=cur
                nxt.prev=new_node
            cur=cur.next
    def add_before_node(self,key,data):
        cur=self.head
        while cur:
            if cur.prev is None and cur.data==key:
                self.prepend(data)
                return
            elif(cur.data==key):
                 new_node=Node(data)
                 prev=cur.prev
                 prev.next=new_node
                 new_node.next=cur
                 new_node.prev=prev
            cur=cur.next
    def delete_node(self,key):
        cur=self.head
        while cur:
            if  cur.data==key and cur is self.head:
                if not cur.next:
                    cur=None
                    self.head=None
                    return
                else:
                    nxt=cur.next
                    cur.next=None
                    nxt.prev=None
                    cur=None
                    self.head=nxt
                    return
            elif(cur.data==key):
                if cur.next:
                    nxt=cur.next
                    prev=cur.prev
                    prev.next=nxt
                    nxt.prev=prev
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    prev=cur.prev
                    prev.next=None
                    cur.prev=None
                    cur=None
                    return
        cur=cur.next
    def reverse(self):
        temp=None
        cur=self.head
        while cur:
            temp=cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur=cur.prev
        if temp:
            self.head=temp.prev
        return
    def remove_duplicates(self):#for unsorted Doubly_Linked_List
        cur=self.head
        values=dict()
        while cur:
            if cur.data not in values:
                values[cur.data]="Noted"
                cur=cur.next
            else:
                self.delete_node(cur)
        cur=cur.next
dllist=DoublyLinkedLists()
dllist.append(1)
dllist.append(2)
#dllist.prepend(2)
dllist.append(3)
#dllist.prepend(1)
#dllist.append(4)
#dllist.append(4)
#dllist.append(4)
dllist.append(4)
#dllist.append(5)
#dllist.append(5)
dllist.append(5)
#dllist.add_before_node(3,"S")
#dllist.add_after_node(2,"A")
dllist.delete_node(2)
#dllist.reverse()
dllist.print_list()
