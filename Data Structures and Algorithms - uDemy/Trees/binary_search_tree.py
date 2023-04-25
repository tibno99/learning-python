#For BST, if child is greater than partent, it goes on the right hand side
#Everight on right is greater than above, everything left is less than above
#O(logn) is n steps to find, remove, add nodes (divide and conquer), but technically its O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root == None: 
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.val == new_node.val : 
                return False
            if new_node.val < temp.val: 
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, val):
        temp = self.root
        while temp is not None:
            if val < temp.left.val:
                temp = temp.left

            elif val > temp.right.val:
                temp = temp.right

            else:
                return True
        
        return False



tree = BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
print(tree.root.val)
print(tree.root.left.val)
print(tree.root.right.val)
contains = tree.contains(3)
print(contains)


