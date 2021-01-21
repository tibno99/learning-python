#Doubly linked list code
#Node class to describe the nodes in this linked list


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
    
    #A private nested node class (add __ as a prefix to make private)
    class Node:
        def __init__(self, data, next, previous):
            self.data = data
            self.next = next
            self.previous = previous
   
    #Clears all values from the list, setting them to None
    def clear(self):
        trav = self.head
        while trav != None:
            nextNode = trav.next
            trav.previous = None
            trav.next = None
            trav.data = None
            trav = nextNode
        
        self.head = self.tail = trav = None
        self.size = 0

    #Returns the size of the list
    def sizeOf(self):
        return self.size

    #Returns whether the list is empty
    def isEmpty(self):
            return self.sizeOf() == 0

    #Adds a value to the end of the list (by default)
    def add(self, elem):
        #If the list is empty, create a new Node and assign it to the tail and header
        if self.isEmpty():
            #This also sets both of these to point towards the same object intially
            self.head = self.tail = self.Node(elem, None, None)
        #If the list is not empty, assign the new data to the tail node
        else:
            #Create the "next node" as a node object with the data being elem and the previous node being a reference to the previous tail
            self.tail.next = self.Node(elem, None, self.tail)
            #Set tail to the last node in the list
            self.tail = self.tail.next
        self.size += 1
       
    #This adds a new node to the start of the list
    def addFirst(self, elem):
        if self.isEmpty():
            self.head = self.tail = self.Node(elem, None, None)
        else:
           #Creates a previous node in the header node
            self.head.previous = self.Node(elem, self.head, None)
            #Sets the header to the new head
            self.head = self.head.previous
        self.size += 1

    def removeFirst(self):
        #If the list is already empty, return a message
        if self.isEmpty() == 1:
            print('List is empty') 
        #Else remove the first node
        else:
            #Set the head node to the next node it referenced
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            #If the size is now 0, set all nodes back to null
            if self.isEmpty() == 1:
                self.head.prev = None
            return data

    def removeLast(self):
        #If the list is already empty, return a message
        if self.isEmpty() == 1:
            print('List is empty') 
        #Else remove the last node
        else:
            #Set the tail node to the previous node it referenced
            data = self.tail.data
            self.tail = self.tail.previous
            self.size -= 1
            #If the size is now 0, set all nodes back to null
            if self.isEmpty() == 1:
                self.tail.next = None
            return data
    
    #Peak to see what the header value is
    def peakFirst(self):
        if self.isEmpty() == 1:
            print('List is empty') 
        else:
            return self.head.data

    #Peak to see what the tail value is
    def peakLast(self):
        if self.isEmpty() == 1:
            print('List is empty')
        else:
            return self.tail.data 

    #Additional methods to add:
    #Find value
    #Remove node @ certain index or value
    #Find the index of a value
    #Can add an iterator
    
   

#TEST

x = DoublyLinkedList()
x.add(27)
x.add(28)
x.addFirst(29)
x.clear()


