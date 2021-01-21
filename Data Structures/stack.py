#Stack Code
from doubly_linked_list import DoublyLinkedList

class Stack():

    #Initialize the stack data using the doubly linked list we created before
    def __init__(self):
        self.data_list = DoublyLinkedList()

    #Reference the sizeOf function from doubly linked lists
    def sizeOf(self):
        return self.data_list.sizeOf()

    def isEmpty(self):
        return self.sizeOf() == 0

    #Add to the top of the stack
    def push(self, elem):
        self.data_list.add(elem)
    
    #Remove from the top of the stack
    def pop(self):
        if self.isEmpty():
            print('List is empty')
        else:
            self.data_list.removeLast()

    #Peak at what is on the top of the stack
    def stackPeak(self):
        return self.data_list.peakLast()

    #Can add an iterator if implemented into doubly linked list
    


    
#TEST
test = Stack()
test.push(1)
test.push(2)
test.pop()
#Output should be 1
print(test.stackPeak())