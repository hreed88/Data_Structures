class Node:
  def __init__(self, data):
    self.item = data
    self.next = None
    self.prev = None

class Deque:
  def __init__(self):
    self.front = None
    self.back = None
    self.size = 0

  def empty(self):
        if(self.size == 0):
            return True
        else:
            return False
        pass

  def get_size(self) -> int:
       return self.size
       pass

  def push_front(self, data):
    tempNode = Node(data)

    if(self.empty()):
       self.front = tempNode
       self.back = tempNode
    else:
       tempNode.next = self.front
       self.front.prev = tempNode
       self.front = tempNode

    self.size += 1   

  def push(self, data):
    tempNode = Node(data)
    if(self.empty()):
       self.front = tempNode
       self.back = tempNode
    else:   
       tempNode.prev = self.back
       self.back.next = tempNode
       self.back = tempNode
    
    self.size += 1

  def pop_front(self):
       tempInt = self.front.item
       self.front = self.front.next
       self.size -= 1
       return tempInt
    
  def pop(self):
       if(not(self.empty())):
         tempInt = self.back.item
         self.back = self.back.prev
         self.back.next = None
         self.size -= 1
         return tempInt
       else:
          return None
    
  def Front(self):
       if(self.empty()):
        return 0
       else:
        return self.front.item
    
  def Back(self):
       if(self.empty()):
          return 0
       else:
        return self.back.item

  def printQ(self):
     current = self.front
     while(current != None):
        print(current.item)
        current = current.next

     
       
def reverse(thisDeque):
   reversedDeque = Deque()
   current = thisDeque.back
   while(current != None):
      reversedDeque.push(current.item)
      current = current.prev
   
   return reversedDeque

if __name__ == '__main__':
   
   myDeque = Deque()

   print(myDeque.empty())

   myDeque.push(11)
   myDeque.push(10)
   print(myDeque.Front())
   myDeque.push_front(14)

   print(myDeque.Front())
   print(myDeque.Back())
   print(myDeque.get_size())
   print(myDeque.empty())

   print(myDeque.pop_front())
   print(myDeque.Front())
   print(myDeque.pop())
   print(myDeque.Back())
   print(myDeque.Front())
#-------------------------------------------------
   reverseQ = Deque()
   reverseQ.push(9)
   reverseQ.push(10)
   reverseQ.push(11)
   reverseQ.push(12)
   reverseQ.printQ()

   reversedQ = reverse(reverseQ)

   reversedQ.printQ()

