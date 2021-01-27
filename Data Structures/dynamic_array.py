#Dynamic Array Code
import numpy as np

#Although python lists are already dynamic, practice making a dynamic array using numpy's .empty static arrays
class DynamicArray:

    #Initialize the dynamic array private variables (add __to these after testing to make private)
    def __init__(self):
        self.len = 0
        self.capacity = 0
        self.arr = []

    #Define a method to create a static array of size n
    def array(self, n):
        if (n < 0): 
            print ('Array size must be greater than zero. Your size was:', n)
        else: 
            self.capacity = n
            self.arr = np.empty(n, object)
    
    #Define a method to return the size of the dynamic array
    def sizeOf(self):
        return self.len

    #Define a method to return whether the dynamic array is empty or not
    def isEmpty(self):
        return self.sizeOf() == 0

    #Returns the value at the index
    def getVal(self, index):
        if index > self.len:
            print('Outside array bound')
        else:
            return self.arr[index]

    #Adds a value to the next empty spot of the array. If the array is full, double the array size and then add the next value in
    def addVal(self, elem):
        if self.len + 1 >= self.capacity:
            self.capacity = self.capacity * 2
            new_arr = np.empty(self.capacity, object)
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.len += 1
        else:
            self.arr[self.len] = elem
            self.len += 1

  
#TEST
x = DynamicArray()
x.array(10)

for i in range(11):
    x.addVal(i)
    print(x.len)
print(x.capacity)


