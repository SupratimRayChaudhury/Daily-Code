


class Node:
    def__init__(self,data): 
        self.data = data 
        self.ref = None
class Linkedlist:
    def__init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node 


LL1=linkedlist()
LL1.print_LL()