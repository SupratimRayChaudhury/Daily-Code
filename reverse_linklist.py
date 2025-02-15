class Node:
    def __init__(self):
        self.data=input("Enter a value:")
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def insert(self):
        new_node=Node()
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

        
    def display(self):
        current_node = self.head
        print('[',id(self.head),']',end='')
        while(current_node):
            if current_node.next is not None:
                x=id(current_node.next)
            else:
                x='None'
            print('->[',current_node.data,'|',x,']',end='')
            current_node = current_node.next
        print("\n")

    def reverse(self):
        current_node=self.head
        s=0
        while(current_node):
            current_node=current_node.next
            s=s+1
        for i in range(s-1):
            position=0
            current_node=self.head
            while(current_node.next.next!=None):
                current_node=current_node.next
            if position==i: 
                current_node.next.next=self.head
                self.head=current_node.next
                current_node.next=None
            else:
                current_node1=self.head
                while(position+1 !=i):
                    position=position+1
                    current_node1=current_node1.next

                current_node.next.next=current_node1.next
                current_node1.next=current_node.next
                current_node.next=None            
ob=linklist()
while(True):
    n=input("1.Insert\n2.Display.\n3.Reverse.\n")
    if n=="1":
        ob.insert()
    elif n=="2":
        ob.display()
    elif n=="3":
        ob.reverse()
    else:
        break