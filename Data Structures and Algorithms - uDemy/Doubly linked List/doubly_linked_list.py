class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail - None
        else:
            self.tail = self.tail.prev
            self.tail.next = temp.next
            temp.prev = None
        
        self.length -=1
       
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail - None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get_value(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,  index, - 1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.val = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get_value(index - 1)
        after = before.next
        before.next = new_node
        after.prev = new_node
        new_node.next = after
        new_node.prev = before
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        temp = self.get_value(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = temp.prev = None

        self.length -= 1
        return temp


        



dll = DoublyLinkedList(1)
dll.append(2)
dll.print_list()
dll.prepend(0)
dll.print_list()
dll.insert(1,7)
dll.print_list()
dll.remove(1)
dll.print_list()

