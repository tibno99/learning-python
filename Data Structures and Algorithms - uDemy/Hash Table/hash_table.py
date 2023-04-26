#Key value pair is ran through hash, returns the key value pair and an address
#These are one way/deterministic
#Big 0, with the assumption of the hash method is good for distribution/large memory space we assume that it is O(1) (to look up or place something by key)


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash =(my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, val):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, val])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys





table = HashTable()
table.set_item('One', 1)
table.set_item('Two', 2)
table.set_item('Three', 3)
table.set_item('Four', 4)
table.set_item('Five', 5)
table.set_item('Six', 6)
table.set_item('Seven', 7)
table.print_table()
print(table.get_item('One'))
print(table.get_item('Eight'))
print(table.keys())