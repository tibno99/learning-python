#Doubly linked list code
class DoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    #Nested node class to describe the nodes in this linked list
    class Node:

        def __init__(self, data, next, previous):
            self.data = data
            self.next = next
            self.previous = previous



x = Node(0,1,2)
print(x.data)