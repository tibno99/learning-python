#Priority Queue Code
#This ADT only works with comparable elements!
import math

class PriorityQueue():

    #Initialize vars
    def __init__(self):
        #The number of elements in the heap
        self.heapSize = 0
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

    #Swaps the values/indexs of two nodes in the heap/hash map
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.hashmap[self.heap[i]], self.hashmap[self.heap[j]] = [i], [j]

    #Add map methods
    def mapAdd(self, val, index):
        

    def mapRemove(self, val, index):

    #Internal method: Bottom up node swim
    def swimUp(self, k):
        #First get the parent of node k
        parent = math.floor((k-1)/2)
        #While k is not the root node and its value is smaller than its parent (min heap)
        while (k > 0) & (self.heap[k] < self.heap[parent]):
            #Switch the value of node k and parent node
            self.swap(k, parent)
            #k now becomes the new parent index
            k = parent
            #Find the new parent of k
            parent = math.floor((k-1)/2)

    def sinkDown(self, k):
        #Keep sinking until we reach one of our break clauses
        while TRUE:
            #Left and right child indicies of k
            left = 2*k + 1
            right = 2*k + 2
            #Assume left index has our smaller node
            smaller = left
            #Verify that the left node is smaller, otherwise assign it to right node
            if (right < self.heapSize) & (self.heap[right] < self.heap[left]):
                smaller = right
            #Break if we are outisde the bounds of the heap or we cannot sinkdown any more
            if (left > self.heapSize) | (self.heap[k] < self.heap[smaller]):
                break
            #Otherwise swap the value of the nodes, then set k to be the new parent node
            self.swap(k, smaller)
            k = smaller

    #For simplicity, assuming only comparable non null values are going to be added to this ADT
    def add(self, elem):
        self.heap.append(elem)
        self.hashmap[elem] = self.heapSize
        self.swimUp(self.heapSize)
        self.heapSize += 1



#TEST
test_PQ = PriorityQueue()
test_PQ.add(56)
test_PQ.add(4)
test_PQ.add(44)
test_PQ.add(55)
test_PQ.add(5)
test_PQ.add(0)
print(test_PQ.heap)
print(test_PQ.hashmap)


    
    

