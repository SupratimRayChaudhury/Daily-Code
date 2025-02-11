class Node:
    def __init__(self):
        self.data=int(input("Enter a value:"))
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

    def middle_node(self):
        fast_node=self.head
        slow_node=self.head
        while(True):
            if fast_node.next!=None:
                if fast_node.next.next!=None:
                    fast_node=fast_node.next.next
                    slow_node=slow_node.next
                else:
                    return slow_node.next.data
                    
            else:
                return slow_node.data
                


ob=linklist()
while(True):
    n=input("1.Insert\n2.Display.\n3.Find middle node.\n")
    if n=="1":
        ob.insert()
    elif n=="2":
        ob.display()
    elif n=="3":
        p=ob.middle_node()
        print("Middle Node is:",p)
    else:
        break