class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
class BinayTree:
    def __init__(self,root):
        self.root=Node(root)
    def print_BinaryTree(self,type):
        if type=="preorder":
            return self.preorder_traversal(self.root,"")
        elif type=="inorder":
            return self.inorder_traversal(self.root,"")
        elif type=="postorder":
            return self.postorder_traversal(self.root,"")
        elif type=="level_order":
            return self.Level_order_traversal(self.root)
        elif type=="reverse_level_order":
            return self.reverse_level_order_traversal(self.root)
        else:
            raise ValueError("Entered Type of traversal "+type+" is Invalid.")
    def inorder_traversal(self,node,traversal):
        if node:
            traversal=self.inorder_traversal(node.left,traversal)
            traversal+=(str(node.value)+"-->")
            traversal=self.inorder_traversal(node.right,traversal)
        return traversal
    def postorder_traversal(self,node,traversal):
        if node:
            traversal=self.postorder_traversal(node.left,traversal)
            traversal=self.postorder_traversal(node.right,traversal)
            traversal+=(str(node.value)+"-->")
        return traversal
    def preorder_traversal(self,node,traversal):
        if node:
            traversal+=(str(node.value)+"-->")
            traversal=self.preorder_traversal(node.left,traversal)
            traversal=self.preorder_traversal(node.right,traversal)
        return traversal
    def Level_order_traversal(self,node):
        if node is  None:
            return
        queue=Queue()
        queue.enqueue(node)
        traversal=""
        while len(queue)>0:
            traversal+=str(queue.peek())+"-->"
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    def reverse_level_order_traversal(self,node):
        if node is None:
            return
        queue=Queue()
        stack=Stack()
        queue.enqueue(node)
        traversal=""
        while len(queue)>0:
            node=queue.dequeue()
            stack.push(node)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        while len(stack)>0:
            node=stack.pop()
            traversal+=str(node.value)+"-->"
        return traversal
    def __max__(self):
        return self.max_element()
    def __min__(self):
        return self.min_element()
    def min_element(self):
        node=self.root
        lst=[]
        lst.append(node)
        min=float("infinity")
        while lst:
            node=lst.pop()
            if node.value<min:
                min=node.value
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        return min
    def find_element(self,ele):
        node=self.root
        lst=[]
        lst.append(node)
        while lst:
            node=lst.pop()
            if node.value==ele:
                return "Element Found"
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        return "Element Not Found"
    def max_element(self):
        node=self.root
        lst=[]
        lst.append(node)
        max=float("-infinity")
        while lst:
            node=lst.pop()
            if node.value>max:
                max=node.value
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
        return max

tree=BinayTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
print(tree.print_BinaryTree("level_order"))
# te=BinayTree("a")
# te.root.left=Node("b")
# te.root.right=Node("c")
# te.root.left.left=Node("d")
# te.root.left.right=Node("e")
# te.root.right.left=Node("f")
# te.root.right.right=Node("g")
# print(te.print_BinaryTree("level_order"))
'''
print(tree.print_BinaryTree("preorder"))
print(tree.print_BinaryTree("inorder"))
print(tree.print_BinaryTree("postorder"))
print(tree.print_BinaryTree("level_order"))
print(tree.print_BinaryTree("reverse_level_order"))
print(tree.min_element())
print(tree.max_element())
print(tree.find_element(6))
'''