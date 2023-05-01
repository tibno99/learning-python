class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self, val):
        new_node = Node(val)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self): 
        temp = self.first
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def enqueue(self, val):
        new_node = Node(val)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

q = Queue(0)
q.enqueue(1)
q.dequeue()
q.print_queue()

