from EECS330_Lab4_PartA_LinkedList import Deque

#Author: Harrison Reed
#Date: 10/9/2023
#Title: EECS_Lab6_BST
#Description: Code for implementing BST, TreeNode, TreeMap, TreeMapNode classes.
#             And testing the functionality of these classes in Main


#Seperate Node Class for the Tree Map
class TreeMapNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

#Tree Map class
class TreeMap:
  def __init__(self):
    self.root = None
  #same as insert for bst
  def put(self, id, value):
     tempNode = TreeMapNode(id, value)
     
     if(self.root == None):
        self.root = tempNode
     else:
        self.putHelper(self.root, tempNode)

  #same as insertHelper for BST, however use key value as the value to store nodes
  def putHelper(self, parent, node):

      if(node.key > parent.key or node.key == parent.key):
        if(parent.right != None):
            self.putHelper(parent.right, node)
        else:
            parent.right = node
      

      if(node.key < parent.key):
        if(parent.left != None):
            self.putHelper(parent.left, node)
        else:
            parent.left = node
  
  #same as search for BST
  def get(self, key):
      tempNode = self.root
      return self.getHelper(tempNode, key)
 
  #same as search for BST, however use key to search for a value in the tree
  def getHelper(self, node, key):    
        if(node == None):
          return None
        if(node.key == key):
          return node.value
        elif(node.key < key):
          return self.getHelper(node.right, key)
        else:
          return self.getHelper(node.left, key)
     
#Node used for BST
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

#Binary Search Tree Class
class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0#Set size to 0 for empty tree

  #return how many elements are in the tree
  def getSize(self):
     tempSize = self.size
     return tempSize
  
  #insert new node into tree
  def insert(self, key):
        newNode = TreeNode(key)
        if(self.size == 0):
          self.root = newNode
        else:
          self.insertHelper(self.root, newNode)#use recursive helper function to insert new node into tree

        self.size += 1 #increment size of tree
  
  #helper function for insert, takes two arguments, the current node(parent), and node to be inserted
  def insertHelper(self, parent, node):
      #If our new value is greater than parent value go to the right side of tree. #
      #Since we allow duplicates in this implementaion, if there is a duplicate we will also head down right side of tree
      if(node.value > parent.value or node.value == parent.value):
        if(parent.right != None):
            #If the current node has a right child. Call our function again with current nodes right child this time
            self.insertHelper(parent.right, node)
        else:
            #if this node doesn't have a right child we can insert our new node
            parent.right = node
      
      #If our new node has a value less then our current node we head down the left side of the tree
      if(node.value < parent.value):
        if(parent.left != None):
            #if current node has left child, call our function again with current nodes left child
            self.insertHelper(parent.left, node)
        else:
            #if current node doesn't have a left child we can insert our new node into the tree
            parent.left = node
      
  
  #Search function that uses recursive helper function to find item in tree
  def search(self, key):
      tempNode = self.root
      return self.searchHelper(tempNode, key)
  
  #helper function for search
  def searchHelper(self, node, key):    
        #if we arrive at an empty node then our key is not in the tree so return None
        if(node == None):
          return None
        #if we find our value return the node at which we found this value
        if(node.value == key):
          return node
        #if the current nodes value is less than key than we call function again with current nodes right child
        elif(node.value < key):
          return self.searchHelper(node.right, key)
        #if the current nodes value is greater than key than we call function again with current nodes left child
        else:
          return self.searchHelper(node.left, key)

#checks if node is a leaf node
  def isLeaf(self, node):
        #if node doesn't have left or right child return true, false otherwise
        if(node.left == None and node.right == None):
          return True
        else:
          return False      

        pass
  
  #Breadth First Search algorithm
  def BFS(self):
    #Create new queue
    myQueue = Deque()
    #create array to store visited nodes
    myVect = []
    #starting node is root
    thisNode = self.root
    #Make sure tree is not empty, if not push current node to queue
    if(thisNode != None):
        myQueue.push(thisNode)
    #while our queue is not empty we will traverse the tree level by level
    while(not(myQueue.empty())):
        #pop the front of the queue, so we can move onto child nodes in next iteration
        thisNode = myQueue.pop_front()
        #make sure left child is not empty, if so we can add it to the queue
        if(thisNode.left != None):
           myQueue.push(thisNode.left)
        #make sure right child is not empty, if so we can add it to the queue
        if(thisNode.right != None):
           myQueue.push(thisNode.right)
        
        #add first element that has been popped from queue (i.e iteration 1 = root, iteration 2 = root->left, root->right, 
        #iteration 3 = root->left->left, root->left->right, root->right->left, root->right->right,..., iteration n = ...)
        #note this is a simpflication of what the code is actually doing. Each loop only appends one node at a time
        #However the way we add items to the queue our array will look like this
        myVect.append(thisNode.value)

    return myVect
     
  



if __name__ == '__main__':
    # Initialize BST.
    bst = BinarySearchTree()

    # Test inserting nodes
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    # Test size method.
    assert bst.getSize() == 7
    assert bst.search(1) == None

    # Test inserting additional nodes.
    bst.insert(1)
    bst.insert(6)

    assert bst.getSize() == 9
    assert bst.search(1).value == 1

    # Finally, also test by inserting duplicate values.

    # Test level order traversal with duplicates.
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(1)
    bst.insert(6)

    # Test level order traversal.
    print(bst.BFS())
    assert bst.BFS() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]

    tree_map = TreeMap()

    # Test putting and getting key-value pairs.
    tree_map.put(3, "A")
    tree_map.put(1, "B")
    tree_map.put(2, "C")
    tree_map.put(4, "D")

    assert tree_map.get(2) == "C"
    print(tree_map.get(2))
    assert tree_map.get(1) == "B"
    print(tree_map.get(1))
    assert tree_map.get(4) == "D"
    print(tree_map.get(4))
    # Non-existent key should return None.
    assert tree_map.get(5) is None
    print(tree_map.get(5))