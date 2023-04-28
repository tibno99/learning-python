#Graph can be represented by adjacency matrix or list
#In the matrix, you need to store all verticies therefore space complexity is O(V^2)
#In the list, you need to store the verticies and their corresponding edges so space complexity is O(V + E)
#Adding verticies is harder in a matrix, it is O(V^2), in the list it is O(1) (hashmap)
#Adding edges is O(1) for both
#Removing edges is O(1) for the matrix and O(E) for the list
#Removing vertix is O(V+E) for a list and a O(V^2) for matrix

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        print(self.adj_list)
      
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 not in self.adj_list[v2]:
                self.adj_list[v2].append(v1)
            if v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
            return True
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edge in self.adj_list[vertex]:
                self.adj_list[edge].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    

    

graph_ = Graph()
graph_.add_vertex('A')
graph_.add_vertex('B')
graph_.add_vertex('C')
graph_.add_vertex('D')
graph_.add_edge('A', 'B')
graph_.add_edge('A', 'C')
graph_.add_edge('A', 'D')
graph_.add_edge('B', 'D')
graph_.add_edge('C', 'D')
graph_.remove_vertex('D')
graph_.print_graph()
