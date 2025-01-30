class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        current = self.root
        parent = None
        while current is not None:
            if value == current.value:
                break
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            successor = self.find_successor(current)
            current.value = successor.value
            self.delete(successor.value)

    def find_successor(self, node):
        if node.right is not None:
            return self.find_min(node.right)

        current = node
        parent = node.parent
        while current == parent.right:
            current = parent
            parent = parent.parent

        return parent

    def find_min(self, node):
        if node.left is None:
            return node
        else:
            return self.find_min(node.left)

    def print_tree(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("The tree is:")
bst.print_tree()

print("Searching for 7:", bst.search(7))
print("Searching for 9:", bst.search(9))

bst.delete(7)

print("The tree after deleting 7:")
bst.print_tree()