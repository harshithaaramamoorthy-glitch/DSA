class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(self.root,value)   

    def insert(self,node,value):
        if value < node.data:
            if node.left is None:
             node.left = Node(value)
            else:
                self.insert(node.left,value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(node.right,value)

    def preorder(self,node):
        if node is None:
            return


        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node is None:
            return    
        
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)

    def postorder(self,node):
        if node is None:
            return    
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")

    def BFS(self):
        if self.root is None:
            return
        
        queue = []
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            print(current.data,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)





b = Tree()
b.insert(1)
b.insert(2)
b.pop()
b.BFS()

