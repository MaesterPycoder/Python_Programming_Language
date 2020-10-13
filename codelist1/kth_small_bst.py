class Node:
    def __init__(self,data=None):
        self.value = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_bst(self):
        if self.root is None:
            return
        stack=list()
        stack.append(self.root)
        while len(stack)>0:
            node=stack.pop()
            print(node.value,end="->")
            if node.left:
                stack.insert(0,node.left)
            if node.right:
                stack.insert(0,node.right)
    
bst=BinarySearchTree()
bst.root=Node(50)
bst.root.left=Node(40)
bst.root.right=Node(30)
bst.root.left.left=Node(5)
bst.root.left.right=Node(10)
bst.root.right.left=Node(15)
bst.root.right.right=Node(20)
bst.print_bst()


