#Code for union find

class UnionFind(size):

    def __init__(self):
        #Number of elements in the union find
        self.size = size
        #unionsize tracks the size of each component
        self.unionsize = []
        #ID points to the parent of i, id[i] = 1 means it is a root node
        self.id = []
        #Number of components in union find
        self.numComponents = 0

    #Creates a union find of a defined size
    def create(self, size):
        if size < 0:
            print('Size cannot be < 0')
            break
        self.numComponents = size
        for i in range(size):
            self.id[i] = i
            self.unionsize[i] = 1

    #Find which union set i belongs to
    def find(self, i):
        #First, find the root of the union set
        root = i
        while(root != self.id[root]):
            root = self.id[root]

        #Compress the path, giving amortized constant time
        while( i != root):
            nextID = self.id[i]
            self.id[i] = root
            i = nextID

    #Returns true if they have the same root from the find function
    def connected(self, i, j):
        return self.find(i) == self.find(j)
    
    #Returns the size of the unionset that i belongs to
    def unionSetSize(self, i):
        return self.unionsize(self.find(i))

    def unify(self, i, j):
        

