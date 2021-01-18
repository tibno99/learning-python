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

    def getVal(self, index):
        if index > self.len:
            print('Outside array bound')
        else:
            return self.arr[index]

  





      
#TEST
x = DynamicArray()
x.array(10)
x.setVal(0,1)
print(x.getVal(0))
