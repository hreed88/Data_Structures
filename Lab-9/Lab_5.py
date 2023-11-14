#Author: Harrison Reed
#Date: 10/2/2023
#Description: Lab-5, problem sets for implementation of disjoint sets

class DisjointSet:
    def __init__(self, size):
        self.vertex = list(range(size))
        self.weight = [1] * size
        self.rank = [1] * size
        self.numBlocks = size #keep track of number of sets 

    def validate(self, v1):
        if (self.vertex[v1] < 0 ):
            return False
        else:
            return True 
        
    def size(self, v1):
        return(self.weight[self.find(v1)])
    
    def height(self, v1):
        return(self.rank[self.find(v1)])
    
    def changeSize(self, v1, v2):
        self.weight[self.find(v1)] += self.weight[self.size(v2)]#Update sze at given index

    def parent(self, v1):
        return self.vertex[v1]

    def find(self, v1):
        #iterate through each vertex until the index of the vertex is the same as vertex[index]
        if self.vertex[v1] != v1:
            self.vertex[v1] = self.find(self.vertex[v1])
        #return the item at the vertex where vertex[v1] == v1
        return self.vertex[v1]
    
    def isConnected(self, v1, v2):
        #if both roots are the same then return true
        if(self.find(v1) == self.find(v2)):
            return True
        else:#return false if otherwise
            return False
        
    def unionByWeight(self, v1, v2):
        
        #if the two verticies have the same root, then they are already in the same set so we dont need to do anything
        if(self.find(v1) == self.find(v2)):
            return
        
        #if the size of set of v1 is greater than the set of v2 add the set of v2 to v1
        if(self.size(v1 )> self.size(v2)):
            self.changeSize(v1, v2)#update size of v1 with v2 before doing union since if it was after union it would assign incorrect size
            self.vertex[self.find(v2)] = self.find(v1)
        else:#otherwise add v1 to v2
            self.changeSize(v2, v1)
            self.vertex[self.find(v1)] = self.find(v2)
    #update number of sets, since we are combining two we subtract 1 from the numBlocks which at prog start is the number of items in the list
        self.numBlocks -= 1
    
    def unionByRank(self, v1, v2):

        #if the two verticies have the same root, then they are already in the same set so we dont need to do anything
        if(self.find(v1) == self.find(v2)):
            return
         #if the height of set of v1 is greater than the set of v2 add the set of v2 to v1
        if(self.height(v1 )> self.height(v2)):
            self.vertex[self.find(v2)] = self.find(v1)
        #else add v1 to v2
        elif(self.height(v1 )< self.height(v2)):
            self.vertex[self.find(v1)] = self.find(v2)
        #otherwise the two verticies have the same height so it doesnt matter which set we add to
        else:
            self.vertex[self.find(v2)] = self.find(v1)
            self.rank[self.find(v1)] += 1

        #update number of sets, since we are combining two we subtract 1 from the numBlocks which at prog start is the number of items in the list
        self.numBlocks -= 1

    #helper functions to see results
    def printVertex(self):
        for i in range(len(self.vertex)):
            print(self.vertex[i], end =",")
    def printSize(self):
        for i in range(len(self.weight)):
            print(self.weight[i], end =",")
    def printHeight(self):
        for i in range(len(self.rank)):
            print(self.rank[i], end =",")

    #unionize the matrix based on if [i][j] = 1
    def joinBlocks(self, connected):
            for i in range(len(connected)):
                for j in range(len(connected[i])):
                    if(connected[i][j] == 1 ):
                        self.unionByWeight(i, j)

    def findBlockSets(self):
        return self.numBlocks
    
    def findblockCount(self, blockId):
        myNum = 0
        for i in range(len(self.vertex)):
            if self.isConnected(self.vertex[i], blockId):
                myNum += 1
        
        if myNum == 0:
            return 1

        return myNum
                

if __name__ == '__main__':
  # Tasks A
  uf = DisjointSet(10)
  # 0 1-2-5-6-7 3-8-9 4
  uf.unionByRank(1, 2)
  uf.unionByRank(2, 5)
  uf.unionByRank(5, 6)
  uf.unionByWeight(6, 7)
  uf.unionByRank(3, 8)
  uf.unionByWeight(8, 9)
  print(uf.isConnected(1, 5))  # true
  print(uf.isConnected(5, 7))  # true
  print(uf.isConnected(4, 9))  # false
  # 0 1-2-5-6-7 3-8-9-4
  uf.unionByWeight(9, 4)
  print(uf.isConnected(4, 9))  # true

  # Tasks B
  Connected = [[1,1,0,1], [1,1,0,0], [0,0,1,1], [1,0,1,1]]
  uf = DisjointSet(4)
  uf.joinBlocks(Connected)
  uf.findblockCount(1)