class Node:
    def __init__(self,value):
        self.data=value
        self.front=None
        self.rear=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        

    def enqueue(self,value):
        new_node=Node(value)
        if self.rear is None and self.front is None:
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.rear=new_node
            self.rear=new_node 
            

    def dequeue(self):

               
     