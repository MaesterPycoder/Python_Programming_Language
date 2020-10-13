class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self, data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=newNode
    def prepend(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def insert_after_node(self,prev,data):
        if not prev:
            raise ValueError("Previous Node Not In The List")
        else:
            newNode=Node(data)
            newNode.next=prev.next
            prev.next=newNode
    def print_list(self):
        cur_node=self.head
        lst=[]
        while cur_node:
            lst.append(cur_node.data)
            cur_node=cur_node.next
        print(lst)
    def delete_node(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node=None
            return
        else:
            prev=None
            while cur_node and cur_node.data!=key:
                prev=cur_node
                cur_node=cur_node.next
            if cur_node is None:
                raise ValueError("Key not present in the list")
            else:
                prev.next=cur_node.next
                cur_node=None
                return
    def delete_node_pos(self,pos):
        cur=self.head
        if pos==0:
            self.head=cur.next
            return
        prev=None
        count=1
        while cur and count!=pos:
            count+=1
            prev=cur
            cur=cur.next
        if cur is None:
            raise ValueError("position doesn't exist")
        prev.next=cur.next
        cur=None
        return
    def length_iter(self):
        count=0
        cur_node=self.head
        while cur_node:
            cur_node=cur_node.next
            count+=1
        return count
    def length_recur(self,node):
        if node is None:
            return 0
        return 1+self.length_recur(node.next)
    def swap_nodes(self,key1,key2):
        if key1==key2:
            return
        prev_1=None
        cur_1=self.head
        while cur_1 and cur_1.data!=key1:
            prev_1=cur_1
            cur_1=cur_1.next
        prev_2=None
        cur_2=self.head
        while cur_2 and cur_2.data!=key2:
            prev_2=cur_2
            cur_2=cur_2.next
        if not cur_1 or not cur_2:
            return
        if prev_1:
            prev_1.next=cur_2
        else:
            self.head=cur_2
        if prev_2:
            prev_2.next=cur_1
        else:
            self.head=cur_1
        cur_1.next,cur_2.next=cur_2.next,cur_1.next
        return
    def reverse_iter(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
    def reverse_recur(self):
        def reverse(cur,prev):
            if not cur:
                return prev
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            return reverse(cur,prev)
        self.head=reverse(cur=self.head,prev=None)
    def merge_sorted_list(self,llist):
        p=self.head
        q=llist.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        else:
            s.next=p
        return new_head
    def remove_duplicates(self):
        cur=self.head
        prev=None
        dup_values=dict()
        while cur:
            if cur.data in dup_values:
                prev.next=cur.next
            else:
                dup_values[cur.data]="Noted"
                prev=cur
            cur=prev.next
    def print_nth_from_last(self,n):
        l=llist.length_iter()
        cur=self.head
        while cur:
            if(l==n):
                print(cur.data)
                return cur.data
            l-=1
            cur=cur.next
            if not cur:
                return 
    def count_occurrence_iter(self,data):
        cur=self.head
        count=0
        while cur:
            if cur.data==data:
                count+=1
            cur=cur.next
        print(count)
        return 
    def count_occurrence_recur(self,node,data):
        if not node:
            return 0
        if node.data==data:
            return 1+self.count_occurrence_recur(node.next,data)
        else:
            return self.count_occurrence_recur(node.next,data)
    def rotate_linkedlist(self,n):
        for _ in range(n):
            cur=self.head
            prev=None
            while cur.next:
                prev=cur
                cur=cur.next
            prev.next=cur.next
            cur.next=self.head
            self.head=cur
    def is_evenlength(self):
        cur=self.head
        while cur and cur.next:
            cur=cur.next.next
            if cur is None:
                print("Yes,even length")
                return 1
        print("No,odd length")
        return 0
    def is_palindrom(self): #Error
        p=self.head
        return
    def sum_of_LinkedLists(self,llist): #Error
        p=self.head
        q=llist.head
        while p or q:
            pass
        pass
    def move_tail_to_head(self):
        llist.rotate_linkedlist(1)
        return
    def rotate(self,k):
        for _ in range(k):
            cur=self.head
            nxt=cur.next
            nde=cur
            while nde.next:
                nde=nde.next
            nde.next=cur
            cur.next=None
            self.head=nxt
    def deleteAlt(self):
        cur=self.head
        prev=self.head
        count=1
        while cur:
            if count%2==0:
                nxt=cur.next
                prev.next=cur.next
                cur=nxt
                count+=1
            else:
                prev=cur
                cur=cur.next
                count+=1
llist=Linkedlist()
llist.append("1")
llist.append("2")
llist.append("3")
llist.append("4")
llist.append("5")
llist.append("6")
llist.deleteAlt()
llist.print_list()
'''
llist.append("E")
llist.append("F")
llist.append("G")
llist.append("H")
llist.append("I")
llist.append("J")
llist.append("K")
llist.append("L")
llist.is_evenlength()'''
'''llist.move_tail_to_head()
llist.print_list()'''
'''llist1=Linkedlist()
llist2=Linkedlist()
llist1.append(2)
llist1.append(3)
llist1.append(4)
llist2.append(5)
llist2.append(6)
llist2.append(7)
llist1.sum_of_LinkedLists(llist2)'''
'''llist=Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist2.append("R")
llist2.append("A")
llist2.append("D")
llist2.append("A")
llist2.append("R")
llist.is_palimdrome()
llist2.is_palimdrome()'''
'''llist.rotate_linkedlist(2)
llist.print_list()'''
'''llist.print_nth_from_last(2)'''
'''llist.append(1)
llist.append(2)
llist.append(1)
llist.append(3)
llist.append(3)
llist.append(1)
llist.append(1)
llist.append(3)
llist.append(5)
llist.append(4)
llist.append(5)
llist.append(6)
llist.count_occurrence_iter(1)
p=llist.count_occurrence_recur(llist.head,1)
print(p)'''
'''llist.remove_duplicates()
llist.print_list()'''
'''llist1=Linkedlist()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)
llist2=Linkedlist()
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)
print("List_1 :")
llist1.print_list()
print("List_2:")
llist2.print_list()
print("Both lists are sorted :")
llist1.merge_sorted_list(llist2)
llist1.print_list()'''
'''llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next,"H")
llist.delete_node("E")
llist.delete_node_pos(3)
llist.swap_nodes("A","H")
llist.reverse_iter()
llist.reverse_recur()
llist.print_list()
print(llist.length_iter())
print(llist.length_recur(llist.head))'''
            
