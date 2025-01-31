class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self):
        if self.val is not None:
            print(self.val,end=", ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.val is not None:
            print(self.val,end=", ")
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.val is not None:
            print(self.val,end=", ")
            
    def display(self):
        print("\nPre Order: ",end="")
        self.preorder()
        print("\nIn Order: ",end="")
        self.inorder()
        print("\nPost Order: ",end="")
        self.postorder()
    

n=BSTNode()


while(True):
    a=input("1.MIN VALUE.\n2.MAX VALUE.\n3.Display.\n4.Search an value.\n5.Insert a value.\n6. Exit\n")
    if a=="1":
        n.get_min(data)
    elif a=="2":
        n.get_max(data)
    elif a=="3":
        n.display(data)
    elif a=="4":
        data=int(input("Enter the search:"))
        n.exists(data)
    elif a=="5":
        data=int(input("Enter the value:"))
        n.insert(data)
    else:
        break