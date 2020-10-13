class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insertNode(value,self.root)
    def _insertNode(self,data,cur):
            if data<cur.data:
                if cur.left is None:
                    cur.left=Node(data)
                else:
                    self._insertNode(data,cur.left)
            elif data>cur.data:
                if cur.right is None:
                    cur.right=Node(data)
                else:
                    self._insertNode(data,cur.right)
            else:
                pass
    def BSTchecker(self):
        if self.root:
            is_bst_satisfied=self._is_bst_checker(self.root,self.root.data)
            if is_bst_satisfied is None:
                return True
            return False
        return True
    def _is_bst_checker(self,cur,data):
        if cur.left:
            if cur.left.data<data:
                return self._is_bst_checker(cur.left,cur.left.data)
            else:
                return False
        if cur.right:
            if cur.right.data>data:
                return self._is_bst_checker(cur.right,cur.right.data)
            else:
                return False
    def search_ele(self,fddata):
        cur=self.root
        while cur:
            if fddata==cur.data:
                return "Found"
            if cur.data>fddata:
                cur=cur.left
            else:
                cur=cur.right
        return "Not Found"
    def min_ele(self):
        cur=self.root
        if cur is None:
            return None
        while cur.left:
            cur=cur.left
        return cur.data
    def max_ele(self):
        cur=self.root
        if cur is None:
            return None
        while cur.right:
            cur=cur.right
        return cur.data
    def successorBST(self):
        cur=None
        if cur.right:
            cur=cur.right
        while cur.left:
            cur=cur.left
        return cur
    def predecessorBST(self):
        cur=None
        if cur.left:
            cur=cur.left
        while cur.right:
            cur=cur.right
        return cur
    def print_bst(self):
        if self.root:
            self._print_bst(self.root)
    def _print_bst(self,cur):
        if cur:
            self._print_bst(cur.left)
            print(cur.data,end="-->")
            self._print_bst(cur.right)
bst=BinarySearchTree()
bst.insert(10)
bst.insert(9)
bst.insert(8)
bst.insert(12)
bst.insert(11)
bst.insert(13)
bst.print_bst()
print(bst.BSTchecker())
tree=BinarySearchTree()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
print(tree.print_bst())
print(tree.BSTchecker())