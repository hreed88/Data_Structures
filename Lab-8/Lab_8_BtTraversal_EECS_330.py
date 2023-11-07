#Author: Harrison Reed
#Date: 11/6/2023
#Description: Tree Traversal section for Lab 8 in EECS_330. Methods contained implement Preorder Traversal, Inorder Traversal, and Postorder Traversal

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
   #Name: isLeaf
   #Description: Checks if a given node is a leaf
   #Return: Bool(True- is a leaf, False- not a leaf)
    def isLeaf(self, thisNode):
       if(thisNode.left == None and thisNode.right == None):
          return True
       else:
          return False

   #Name: preorder_traversal
   #Desciption: Driver function for preorder traversal
   #return: List(Containting which nodes are visited in preorder)
    def preorder_traversal(self) -> list:
        myTraversal = []
        currItem = self.root#set starting item to root becasue preorder node->left subtree-> right subtree

        myTraversal.append(currItem.value)#insert current node
        self.preorderHelper(currItem.left, myTraversal)#call recursive to our left subtree
        self.preorderHelper(currItem.right, myTraversal)#call recursive to our right subtree

        return myTraversal
        pass
   
   #Name: preorderHelper
   #Description: recursive helper function that traverses the entire tree
   #reuturn: None
    def preorderHelper(self, currNode, thisTraversal):
       #Makes sure we are not at a NULL node
       if(currNode != None):
        #If not add it to our lsit
        thisTraversal.append(currNode.value)
        #If current node is none or is a leaf return, as we have reached the end of the subtree
       if(currNode == None or self.isLeaf(currNode)):
          return
       #go through subtree of left then right
       self.preorderHelper(currNode.left, thisTraversal)
       self.preorderHelper(currNode.right, thisTraversal)
       pass
    
    #Name: inorder_traversal
    #Desciption: Driver function for preorder traversal
    #return: List(Containting which nodes are visited in inorder)
    def inorder_traversal(self) -> list:
        myTraversal = []
        currItem = self.root

        #Here we want to traverse the tree like left subtree-> node -> right subtree
        self.inorderHelper(currItem.left, myTraversal)#recursive call
        myTraversal.append(currItem.value)
        self.inorderHelper(currItem.right, myTraversal)

        return myTraversal
        pass
    
   #Name: inorderHelper
   #Description: recursive helper function that traverses the entire tree
   #reuturn: None
    def inorderHelper(self, currNode, thisTraversal):
       #Here we want to traverse the tree like left subtree-> node -> right subtree
       if(currNode.left != None):
        self.inorderHelper(currNode.left, thisTraversal)
       if(currNode != None):
        thisTraversal.append(currNode.value)
       if(currNode.right != None):
        self.inorderHelper(currNode.right, thisTraversal)
       if(currNode == None or self.isLeaf(currNode)):
          return
       
       
       pass
    
    #Name: postorder_traversal
    #Desciption: Driver function for postorder traversal
    #return: List(Containting which nodes are visited in postorder)
    def postorder_traversal(self) -> list:
        myTraversal = []
        currItem = self.root

        #Here we want to traverse the tree like left subtree -> right subtree -> node
        self.postorderHelper(currItem.left, myTraversal)#recursive call
        self.postorderHelper(currItem.right, myTraversal)
        myTraversal.append(currItem.value)

        return myTraversal
        pass
    
   #Name: postorderHelper
   #Description: recursive helper function that traverses the entire tree
   #reuturn: None
    def postorderHelper(self, currNode, thisTraversal):
       #Here we want to traverse the tree like left subtree -> right subtree -> node
       if(currNode.left != None):
        self.postorderHelper(currNode.left, thisTraversal)
       if(currNode.right != None):
        self.postorderHelper(currNode.right, thisTraversal)
       if(currNode != None):
        thisTraversal.append(currNode.value)
       if(currNode == None or self.isLeaf(currNode)):
          return
       
       
       pass

#Name: Main
#Description: Main funtion to test our traversal methods
if __name__ == '__main__':
   bt = BinaryTree()
   bt.root = TreeNode(1)
   bt.root.left = TreeNode(2)
   bt.root.right = TreeNode(3)
   bt.root.left.left = TreeNode(4)
   bt.root.left.right = TreeNode(5)
   bt.root.right.left = TreeNode(6)
   bt.root.right.right = TreeNode(7)
   bt.root.left.left.left = TreeNode(8)
   bt.root.left.left.right = TreeNode(9)
   bt.root.right.right.right = TreeNode(10)

# Test the traversals
   print("Preorder Traversal:", bt.preorder_traversal())
   print("Inorder Traversal:", bt.inorder_traversal())
   print("Postorder Traversal:", bt.postorder_traversal())