class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    #Operations that can be performed on singly linked lists are:
    #1.Traversing of Singly linked List
    def listLength(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    #2.Inserting an element into list
    #Insert at begining
    def insertAtBegining(self,data):
        newNode=Node()
        newNode.setData(data)
        if(self.length==0):
            self.head=newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
        self.length+=1
    #Inserting at End
    def insertAtEnd(self,data):
        newNode=Node()
        newNode.setData(data)
        current=self.head
        while current.getNext() !=None:
            current=current.getNext()
        current.setNext(newNode)
        self.length+=1
    #Inserting at middle
    def insertAtMiddle(self,pos,data):
        newNode=Node()
        newNode.setData(data)
        if(pos==0):
            self.insertAtBegining(data)
        elif(pos>self.length or pos<0):
            return None
        elif(pos==self.length):
            self.insertAtEnd(data)
        else:
            newNode=Node()
            newNode.setData(data)
            count=0
            current=self.head
            while count<pos-1:
                count+=1
                current=current.getNext()
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            self.length+=1
        #3.Deleting an elemnt in list
        #Deleting from begining
        def deleteFromBegining(self):
            if(self.length==0):
                raise ValueError("The list is empty")
            else:
                self.head=self.head.getNext()
                self.length-=1
        #Deleting at End
        def deleteLastNode(self):
            if(self.length==0):
                raise ValueError("This list is empty")
            else:
                currentnode=self.head
                previousnode=self.head
                while(currentnode.getNext()!=None):
                    previousnode=currentnode
                    currentnode=current.getNext()
                previousnode.setNext(None)
                self.length-=1
        #Deleting an intermediate Node
        def deleteFromIntermediate(self,pos):
            if(self.length==0):
                raise ValueError("List is Empty")
            elif(pos<0 or pos>self.length):
                raise ValueError("Position Doesn't exit")
            else:
                currentnode=self.head
                previousnode=self.head
                count=0
                while currentnode.getNext()!=None or count<pos:
                    count+=1
                    if(count==pos):
                        previousnode.setNext(currentnode.getNext())
                        self.length-=1
                    else:
                        previousnode=currentnode
                        currentnode=currentnode.getNext()
        #deleting singly Linked List
        def clear(self):
            self.head=None
                
                    
                    
                
                
                
        
        
    
