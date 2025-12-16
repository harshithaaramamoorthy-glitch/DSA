class node:
    def _init_(self,value):
        self.data = value
        self.prev = None
class linkedlist:  
    def _init_(self):
        self.head = None   
        
    def add_at_end(self,value):
        new_node = node(value) 
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while (current.next is not None):
                current = current.next
            current.next=new_node
            new_node.prev=current
            
    def dis(self):
        if self.head is None:
            print("list is empty")
            return
        current = self.head
        while (current is not None):
            print(f" {current.data}" ,end = '')
            current = current.next
    def add_at_beginning(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
ll = linkedlist()
ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_end(30)
display = ll.dis()



