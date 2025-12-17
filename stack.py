class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value): 
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.isEmpty():
            print("stack underflow")
        else:
            self.head = self.head.next
    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            print(f"Top value is {self.head.data}") 
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        current = self.head
        while (current is not None):
            print(f" {current.data}" ,end = '')
            current = current.next 
    def isEmpty(self):
        if self.head is None:
            return True
        return False
               

s = Stack()
s.push(10)
s.push(20)
s.peek()
display = s.display()
               

            
            



        