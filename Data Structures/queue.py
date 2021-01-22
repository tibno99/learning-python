#Queue code
from doubly_linked_list import DoublyLinkedList

#Code for queue, very straight forward, using elements from doubly linked list to create a queue data structure
class Queue():

    def __init__(self):
        self.data = DoublyLinkedList()

    def sizeOf(self):
        return self.data.sizeOf()

    def isEmpty(self):
        return self.data.sizeOf() == 0
    
    def peek(self):
        return self.data.peakFirst()

    def poll(self):
        self.data.removeFirst()

    def offer(self, val):
        self.data.add(val)

#Test
test_queue = Queue()
test_queue.offer(1)
test_queue.offer(2)
print(test_queue.peek())



     
    


