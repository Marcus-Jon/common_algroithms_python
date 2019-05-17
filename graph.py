class vertex:
    def __init__(self, node):
        # id (usually string) to identify the node
        # dictionary used to keep track of the connections to the nodes
        self.id = node
        self.adjacent = {}

    def __str__(self):
        # used by print function to create an informal representation of the data
        # allows for the setting of a format
        return 'connections: ' +  str ([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        # adds weight value to the neighbor position in the adjacent dictionary
        self.adjacent[neighbor] = weight

    def get_connections(self):
        # returns the keys that are in the adjacent dictionary
        return self.adjacent.keys()

    def get_id(self):
        # return the id for the node
        return self.id

    def get_weight(self, neighbor):
        # gets the weight from the adjacent dictionary using the neighbor variable
        return self.adjacent[neighbor]

class graph:
    def __init__(self):
        # initialise the vert_dict (dictionary) and the number of vertices
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        # used to make an iterator from the iterable vert_dict
        # Defines next() method for what willl come next when iterating through the dict
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        # increase the total of vertices in the graph
        # call to the vertex class, and new vertex is then added to the dictionary of verticies
        # returns the new vertex
        self.num_vertices = self.num_vertices + 1
        new_vertex = vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to , cost = 0):
        # checks to see if the vertex is in the vert_dict, and add it if not
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        # adds the connection between the vertices and assigns a weight
        # makes call to add_neighbor
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


# creating the nodes and edges in the graph
if __name__ == '__main__':

    g = graph()
    # add all the vertices for the graph
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    # add the edges between the vertices and the weight that is assigned to it
    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    # loop through the nodes in the graph
    for v in g:
        # loop through all the connections for that node
        # call to get_connections to get all the connections for the current node
        for w in v.get_connections():
            # assign the current node and connection to variables
            vid = v.get_id()
            wid = w.get_id()
            # print out the node, connection and the weight of that edge
            # call to get_weight, passing over 'w', to get weight of the connection
            print '( %s, %s, %3d)' % (vid, wid, v.get_weight(w))

    # loop through all the nodes and print all the connections for that node
    for v in g:
        # call to get_id to get the current node
        # call to __str__ to print all the connections for that node
        print '[%s] = %s' % (v.get_id(), g.vert_dict[v.get_id()])
