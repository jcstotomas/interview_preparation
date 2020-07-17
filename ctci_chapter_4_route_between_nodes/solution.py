# route between two nodes

# find if there exists a route between two nodes

# normal graph traversal
# breadth first search

# assume there's no cycles

# from the starting node, add it's children
# once you add all its children to the queue, pop hte queue and repeat until
# there is no more children to check
# if there is no more children to check and then return false
# if the node found does in fact have a route and one of the children is equal return true




from collections import defaultdict 
   
#This class represents a directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
       
    def isReachable(self, s, d):
        visited_nodes = set()
        visited_nodes.add(s)
        queue = []
        queue.append(s)

        while queue:
            pop_value = queue.pop()
            for vert in self.graph[pop_value]:
                if d == vert:
                    return True
                if vert not in visited_nodes:
                    visited_nodes.add(vert)
                    queue.append(vert)

        return False


g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)


print(g.isReachable(3,1))
