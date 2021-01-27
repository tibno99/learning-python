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
        self.mapSwap(self.heap[i], self.heap[j])

    #Adds a value to the hashmap
    def mapAdd(self, key, value):
        if key in self.hashmap:
            self.hashmap[key].append(value)
            #print('Key exists: ',self.hashmap[key])
        else:
            self.hashmap[key] = [value]
            #print('Key did not exist:', self.hashmap[key])

    #Removes a value from the hashmap
    def mapRemove(self, key):
        removedVal = self.hashmap[key].pop(0) 
        if self.hashmap[key] == []:
            self.hashmap.pop(key, None)
        return removedVal

        
    #Swaps two values on the hashmap
    def mapSwap(self, key1, key2):
        value1 = self.mapRemove(key1)
        value2 = self.mapRemove(key2)
        self.mapAdd(key1, value2)
        self.mapAdd(key2, value1)

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
        while 1:
            #Left and right child indicies of k
            left = 2*k + 1
            right = 2*k + 2
            #Assume left index has our smaller node
            smaller = left
            #Verify that the left node is smaller, otherwise assign it to right node
            if (right < self.heapSize):
                if (self.heap[right] < self.heap[left]):
                    smaller = right
            #Break if we are outisde the bounds of the heap or we cannot sinkdown any more
            if (left > self.heapSize):
                break
            if  (self.heap[k] < self.heap[smaller]):
                break
            #Otherwise swap the value of the nodes, then set k to be the new parent node
            self.swap(k, smaller)
            k = smaller

    #For simplicity, assuming only comparable non null values are going to be added to this ADT
    def add(self, elem):
        self.heap.append(elem)
        self.mapAdd(elem, self.heapSize)
        self.swimUp(self.heapSize)
        self.heapSize += 1
        #print('Heap Size: ', self.heapSize)

    #Remove a particular element
    def removeAt(self, index):
        if self.isEmpty():
            return 
        #Swap the node at the specified index with the last node in the heap
        self.swap(index, self.heapSize - 1)
        removed = self.heap.pop(self.heapSize - 1)
        self.heapSize -= 1
        elem = self.heap[index]
        self.mapRemove(removed)
        self.sinkDown(index)
        if self.heap[index] == elem:
            self.swimUp(index)
        return removed



#TEST
test_PQ = PriorityQueue()
test_PQ.add(5)
test_PQ.add(4)
test_PQ.add(3)
test_PQ.add(2)
test_PQ.add(1)
test_PQ.removeAt(2)
print(test_PQ.heap)
print(test_PQ.hashmap)


    
    

