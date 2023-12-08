#Author: Harrison Reed
#Date: 11/6/2023
#Description: Graph Traversal section for Lab 8 in EECS. Methods contained implement add_edge, depth first search and breadth first search

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    #Name: add_edge
    #Description: Adds an edge to the adjacency list
    def add_edge(self, u, v):
        #Since its an undirected graph add both adjancencys
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        pass
    
    #Name: printAdjList
    #Description: Prints out our adjacency list
    def printAdjList(self):
        for i in range(len(self.adjacency_list)):
            print(i , ":" , self.adjacency_list[i])

    #Name: dfs
    #Description: Driver function to find the depth first path from given node
    #Return: returns the order in which items are visited as a list
    def dfs(self, source):
        isVisited = []
        self.dfsHelper(source, isVisited)#recursive call
        return isVisited
        pass
    
    #Name: dfsHelepr
    #Description: Recursive method to help dfs method, to traverse a graph in a depth first manner
    #return: None
    def dfsHelper(self, currNode, visitedList):
        #Add current item to our visited nodes
        visitedList.append(currNode)
        #if our nodes neihbors are a sublist of our visited list then we return, because this means all the neighbors have been visited
        if(self.isSublist(visitedList, self.adjacency_list[currNode])):
            return
        
        #Check each neighbor of currNode
        for i in range(len(self.adjacency_list[currNode])):
            #If currNode neighbor that were checking at i is not visited, the recursivly call dfs helper on currNode neighbor at i
            if self.adjacency_list[currNode][i] not in visitedList:
                self.dfsHelper(self.adjacency_list[currNode][i], visitedList)
        pass
    
    #Name: bfs
    #Description: Driver function to find the breadth first path from given node
    #Return: returns the order in which items are visited as a list
    def bfs(self, source):
        myQueue = []
        isVisited = []
        #add current item to our queue
        myQueue.append(source)
        #We have visited this node
        isVisited.append(source)
        #Loop until my queue is empty, i.e all neighbors have been visited
        while(len(myQueue) != 0):
            #placeholder for the node we want to check
            tempVal = myQueue[0]
            #remove current item from our queue
            myQueue.pop(0)
            #Check all neighbors
            for i in range(len(self.adjacency_list[tempVal])):
                #if neighbor is not visited then we push them to our queue, and say we have visited them
                if self.adjacency_list[tempVal][i] not in isVisited:
                    myQueue.append(self.adjacency_list[tempVal][i])
                    isVisited.append(self.adjacency_list[tempVal][i])

        return isVisited
        pass
    #Name: isSublist
    #Description: Checks if mySubList, is a sub list of myList
    def isSublist(self, myList, mySubList):
        for i in range(len(myList) - len(mySubList) + 1):
            if(myList[i: i + len(mySubList)] == mySubList):
                return True
        return False

#Name: Main
#Description: Main function to test our graph traversal methods
if __name__ == '__main__':
# Create a graph with 20 vertices
    graph = Graph(20)

# Add edges (change as needed)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    graph.add_edge(4, 9)
    graph.add_edge(4, 10)
    graph.add_edge(5, 11)
    graph.add_edge(5, 12)
    graph.add_edge(6, 13)
    graph.add_edge(6, 14)
    graph.add_edge(7, 15)
    graph.add_edge(7, 16)
    graph.add_edge(8, 17)
    graph.add_edge(8, 18)
    graph.add_edge(9, 19)

    graph.printAdjList()

    print("DFS from vertex 0:", graph.dfs(0))
    print("BFS from vertex 0:", graph.bfs(0))
