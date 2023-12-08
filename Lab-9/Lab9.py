#Author: Harrison Reed
#Name:Lab9.py
#Date: 11/13/2023
#Description: Program for Lab 9 for EECS, Where we implement Dijkstras shortest path algorithm
#             Prim's Minimum Spanning Tree algorithim, and Kruskal's Minimum Spanning Tree Algorithm

import sys
from queue import PriorityQueue
from Lab_5 import DisjointSet

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    #Name: Dijkstra
    #Description: Path finding algorithm to find the shortest path from a given source node, to all other nodes in the graph
    #Input: src-The node that we use to find paths to other nodes
    #Output: Returns the given distances to reach all other nodes in the graph as a list
    def dijkstra(self, src):
        # Stores shortest distance.
        #Initalize all values to appx. inf(i.e we dont know how far each node is)
        distTo = [sys.maxsize] * self.V
        # Shortest distance to the same node is 0.
        distTo[src] = 0
        #Priority queue to store which nodes have least distance from the source node
        myPQ = PriorityQueue()
        # Your code
        #push all nodes to the priority queue as all of them at the start are appx inf away from source node
        for i in range(len(distTo) + 1):
            if i < len(distTo):
                myPQ.put(i, distTo[i])
        #while the queue is not empty(i.e we still have nodes to visit) we check and see if the given node has a shorter path somewhere in the graph
        while(not(myPQ.empty())):
            #get the top of the queue(i.e the node with that has the least weight that has not been visited)
            p = myPQ.get()
            #Check each node that might be connected to p
            for i in range(len(distTo)):
                #get the weight of node(i)
                w = self.graph[p][i]
                #if the weight is not 0(i.e the node is connected to p)
                if( w != 0):
                    #if the distance to the current node is less than the weight of p -> i + the distance to p (src->p)
                    if(distTo[i] >  w + distTo[p]):
                        #than we change the distance to i as a shorter path has been found
                        distTo[i] = distTo[p] + w
                        #add i back into the PQ as this might affect the paths to nodes connected to i
                        myPQ.put(i, distTo[i])
        # You have to call print_solution by passing dist.
        # In this way everyone's output would be standardized.
        self.print_dijkstra(distTo)


    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")
    #Name: getSmallest
    #Description: Helper function for prim, get the smallest edge possible given an array of 
    #             connected edges and an array containing if an array has been visited or not
    #Returns the smallest item possible
    def getSmallest(self, smallestEdge, currVis):
        thisItem = sys.maxsize
        for i in range(self.V):
            if(smallestEdge[i] < thisItem and not(currVis[i])):
                thisItem = smallestEdge[i]
                smallestItem = i

        return smallestItem

    #Name: prim
    #Description: Path finding algorithm to find the minimum spanning tree for a given graph, using prims algorithm
    #Input: None
    #Output: Returns the minimum spanning tree as an array
    def prim(self):
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        result = [None] * self.V
        #Bool array to store whether an array at given index has been visited or not
        isVisited = [False] * self.V
        #stores the minimimum paths for each node, we use this to keep track of what to visit next
        minList = [sys.maxsize] * self.V

        #Src is connected to itself
        minList[0] = 0
        #Same for result, path is = 0
        result[0] = 0

        #Check all verticies 
        for i in range(self.V):
            
            #Get the smallest possible edge that we should traverse next
            u = self.getSmallest(minList, isVisited)
            #Since we are visiting u we set its value to true in the visited array
            isVisited[u] = True

            #Check all nodes that are connected to u that
            #if
            #1)We find a node that has a smaller edge than the current minimum for that node
            #2)and we have not visited this node
            #3)and the node is connected to the current node(i.e self.graph[u][j] != 0)
            #Then we update the minimum value for that node
            #and set the result of the node at j = to u, since that is the way we are traversing
            for j in range(self.V):
                if (minList[j] > self.graph[u][j]and not(isVisited[j]) and self.graph[u][j] > 0 ):
                    minList[j] = self.graph[u][j]
                    result[j] = u 
            #print(minList)
            
        # Your code.
        # You have to call print_solution by passing the output graph.
        # In this way everyone's output would be standardized.
        self.print_prim(result)

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
                print(f"{result[i]} -> {i} \t {self.graph[i][result[i]]}")

    #Name: Kruskal_mst
    #Description: Path finding algorithm to find the minimum spanning tree for a given graph, using Kruskals algorithm
    #Input: None
    #Output: Returns the minimum spasnning tree as an array
    def kruskal_mst(self):
        # Your code.
        #Disjoint set to store values that are in the path(i.e nodes we have visited)
        myDJS = DisjointSet(self.V)
        #resulting path with its src,dest, weight
        result = []*self.V
        #Queue to store what order we want to check the nodes
        myQueue = []

        #Insert all the nodes that are connected to each other with their weights into the queue(queue.push[src, dest, weight])
        #Ignore the case where [dest, src, weight] are already in the queue because this is undiredicted graph, so we dont care about those cases
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if(self.graph[i][j] > 0 and [j,i, self.graph[j][i]] not in myQueue):
                        myQueue.insert(0,[i,j,self.graph[i][j]])
        #Sort the queue based on the smallest values of the edges in the queue to the largest
        list.sort(myQueue,key=lambda x:x[2])

        #Check all the items in the queue
        while(len(myQueue) != 0):
            #remove item from the queue, and store it in temp item. This is because this is the current path we are on
            tempItem = myQueue.pop(0)
            #If the src and dest are not connected in our disjoint set, then it is not apart of the minSpanning tree
            if(not(myDJS.isConnected(tempItem[0],tempItem[1]))):
                #insert our temp item into the back of the list
                result.insert(len(result),tempItem)
                #union the src and dest nodes as that path has now been visited
                myDJS.unionByWeight(tempItem[0],tempItem[1])
        # Similar to the previous e.g. print your
        # resulting graph.
        self.print_kruskal(result)

    def print_kruskal(self, result):
        print("Edge \t Weight")
        # Note that the below code is slightly different than the Prim's.
        # You can change this print code according to your choice, but
        # you have to display your graph in (vertex->vertex weight) format.
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")

    def printGraph(self):
        print(self.graph)
        print(len(self.graph[0]))

#Name: main
#Description: Main funtion to test functionallity of our implementaions of path finding algorithms
if __name__ == '__main__':

    graph = Graph(21)
    
# Add edges and their weights.
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 5, 2)
    graph.add_edge(4, 6, 2)
    graph.add_edge(5, 7, 2)
    graph.add_edge(7, 8, 2)
    graph.add_edge(6, 8, 2)

    graph.add_edge(8, 9, 5)
    graph.add_edge(8, 10, 4)
    graph.add_edge(9, 11, 3)
    graph.add_edge(10, 11, 1)

    graph.add_edge(11, 12, 1)
    graph.add_edge(12, 13, 1)
    graph.add_edge(13, 14, 1)

    graph.add_edge(14, 15, 1)
    graph.add_edge(14, 16, 10)
    graph.add_edge(15, 17, 1)
    graph.add_edge(16, 20, 1)
    graph.add_edge(17, 18, 1)
    graph.add_edge(18, 19, 1)
    graph.add_edge(19, 20, 1)
    print("Dijksta's__________________________________________")
    graph.dijkstra(0)
    print("Prim's__________________________________________")
    graph.prim()
    print("Kruskal's__________________________________________")
    graph.kruskal_mst()

    
