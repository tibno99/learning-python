#For BST, if child is greater than partent, it goes on the right hand side
#Everight on right is greater than above, everything left is less than above
#O(logn) is n steps to find, remove, add nodes (divide and conquer), but technically its O(n)
#Added some recursive methosd to the BST class


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
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.val:
            return True
        if value < current_node.val:
            return self.__r_contains(current_node.left, value)
        if value > current_node.val:
            return self.__r_contains(current_node.right, value)    

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.val:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.val:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_delete(self, current_node, value):
        #Value not found
        if current_node == None:
            return None
        #Traverse left
        if current_node.val < value:
            current_node.left = self.__r_delete(current_node.left, value)
        #Traverse right
        if current_node.val > value:
            current_node.right = self.__r_delete(current_node.right, value)
        #Value found
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.val = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)

        return current_node

    def r_delete(self, value):
         return self.__r_delete(self.root, value)
       
    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.val




tree = BinarySearchTree()
tree.r_insert(2)
tree.r_insert(1)
tree.r_insert(3)
tree.r_insert(4)
tree.r_insert(5)
print(tree.r_contains(3))
tree.r_delete(5)
print(tree)



