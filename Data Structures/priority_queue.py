#Priority Queue Code
#This ADT only works with comparable elements!
import math

class PriorityQueue():

    #Initialize vars
    def __init__(self):
        #The number of elements in the heap
        self.heapSize = 0
        #The internal capacity of the heap
        self.heapCapacity = 0
        #A list to track the elements in our heap. Using a min heap in this example (root node is lowest)
        self.heap = []
        #The map itself
        self.hashmap = {}

    #If the queue is empty
    def isEmpty(self):
        return self.heapSize == 0

    #Return size of queue
    def sizeOf(self):
        return self.heapSize

    #Internal method: Compare the value of two nodes
    def compare(self,i, j):
        if self.heap[i] > self.heap[j]:
            return 1
        elif self.heap[i] < self.heap[j]:
            return -1
        else:
            return 0
    
    #Internal method: Bottom up node swim
    def swimUp(self, k):
        #First get the parent of node k
        parent = math.floor((k-1)/2)
        #While k is not the root node and its value is smaller than its parent (min heap)
        while (k > 0) & (self.heap[k] < self.heap[parent]):
            #Switch the value of node k and parent node
            self.heap[k], self.heap[parent] = self.heap[parent], self.heap[k]
            #k now becomes the new parent index
            k = parent
            #Find the new parent of k
            parent = math.floor((k-1)/2)

    def sinkDown(self, k):
        #Left and right child indicies of k
        left = 2*k + 1
        right = 2*k + 2
        #Assume left index has our smaller node
        less = left


#TEST
test_PQ = PriorityQueue()
test_PQ.heap = [5, 4, 3, 2, 1, 0]
test_PQ.swimUp(4)
print(test_PQ.heap)



    
    

