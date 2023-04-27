class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):

        # Print the adjacency list of each vertex after sorting it
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):

        # Add the vertex as a key if it does not exist already
        # if it exists then do nothing and return False (failure to add)
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):

        # Check if vertex v1 is a valid vertex and v2 is a valid vertex
        # if they are valid then add the edge between them
        # if not then do nothing and return False (failure to add)
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):

        # Check if vertex v1 is a valid vertex and v2 is a valid vertex
        # if they are valid then remove the edge between them
        # if not then do nothing and return False (failure to remove)
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):

        # if the vertex is not in the graph then do nothing and return False
        # if the vertex is in the graph then remove the vertex and all edges
        # connected to it and return True
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')


print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')


print('\nGraph after remove_vertex():')
my_graph.print_graph()
