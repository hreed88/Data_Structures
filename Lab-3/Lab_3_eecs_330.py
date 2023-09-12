#Linked list Implimentation

class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item # int
            self.next = next_node # IntNode
            
    def __init__(self):
        self.first = None # initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    def insert (self, item, posistion):
        temp = self.first
        if(posistion == 0):
            newNode = self.IntNode(item, temp)
            self.first = newNode
        else:
            for i in range(posistion - 1):
                if(temp.next != None):
                    temp = temp.next
            newNode = self.IntNode(item, temp.next)
            temp.next = newNode

    def reverse(self):
        
        temp1 = self.first
        prev = None
        nextPointer = temp1.next
        while(temp1 != None):
            temp1.next = prev
            prev = temp1
            temp1 = nextPointer
            if(nextPointer != None):
                nextPointer = nextPointer.next
        self.first = prev    

    def replicate(self):
        newList = SLList()

        temp = self.first

        j = 0
        while(temp != None):
           temp2 = temp.next
           for i in range(temp.item):
               newList.insert(temp.item, j )
               j += 1
           temp = temp.next
 
        return newList


    def equals(self, compList):
        temp = self.first
        temp2 = compList.first

        while(temp != None or temp2 != None):
            if(temp == None and temp2 != None):
                return False
            elif(temp2 == None and temp != None):
                return False
            elif(temp.item != temp2.item):
                return False
            
            
            temp = temp.next
            temp2 = temp2.next
        
        return True

    def printList(self):
        temp = self.first
        while(temp != None):
            print(str(temp.item) + " -> ", end="" )
            if(temp.next == None):
                print("NULL", end="")
            temp = temp.next
        print()

if __name__ == '__main__':
  L = SLList()
  L.addFirst(15)
  L.addFirst(10)
  L.addFirst(5)
  #L.insert(12,12)
  L.reverse()

  Lcopy = L.replicate()



  L_expect = SLList()
  L_expect.addFirst(15)
  L_expect.addFirst(10)
  L_expect.addFirst(5)

  L_expect2 = SLList()
  L_expect2.addFirst(5)
  L_expect2.addFirst(10)
  L_expect2.addFirst(15)	

  L.printList()
  Lcopy.printList()

  if L.equals(L_expect):
    print("Two lists are equal, tests passed")
  else:
    print("Two lists are not equal, tests failed")

  if L.equals(L_expect2):
    print("Two lists are equal, tests passed")
  else:
    print("Two lists are not equal, tests failed")