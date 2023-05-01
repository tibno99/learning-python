class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.top == None:
            return None
        else: 
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
        
        


new_stack = Stack(0)
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.print_stack()
temp = new_stack.pop()
new_stack.print_stack()