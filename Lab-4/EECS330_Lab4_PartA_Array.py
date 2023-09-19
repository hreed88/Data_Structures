import numpy as np


class Deque:
  def __init__(self, capacity=10):
    self.capacity = capacity
    # Initialize front and rear pointers.
    self.front = -1
    self.back = -1
    # Initialize size of the deque.
    self.size = 0
    # Use a zero intialized NumPy array to store elements.
    self.array = np.zeros(self.capacity, dtype=object)
  def empty(self):
    return(self.size == 0)
  def get_size(self):
    return self.size
  def push_front(self, data):
      
      if(self.empty()):
        self.front = 0
        self.array[0] = data
        self.size += 1
      else:
        self.size += 1
        if(self.size == self.capacity):
          self.resize()
        self.array = np.roll(self.array, 1)
        self.array[self.front] = data
        #np.concatenate(( [data],self.array))
        #print(self.array[0])
        #np.insert(self.array, 0, data)
      


  def push(self, data):
    self.size += 1
    if(self.empty()):
      self.front = 0
      self.back = 0
    if(self.size  == self.capacity):
      self.resize()
    self.back += 1
    self.array[self.back] = data
  
  def pop_front(self) -> int:
    tempInt = self.array[self.front]
    self.size -= 1
    self.front += 1
    
    return tempInt
  def pop(self) -> int:
    tempInt = self.array[self.back]
    self.back -= 1
    self.size -= 1
    return tempInt
  def peek_front(self) -> int:
    return self.array[self.front]
  def peek(self) -> int:
    return self.array[self.back]
  def resize(self):
    new_capacity = self.capacity * 2
    newArr = np.zeros(new_capacity, dtype=object)

    for i in range(self.capacity):
      newArr[i] = self.array[i]

    self.array = newArr
    self.capacity = new_capacity
  
def is_palinddrome( thisString):
  tempQ = Deque()
  for i in range(len(thisString)):
    tempQ.push(thisString[i])

  counter = 0
  while(not(tempQ.empty())):
      if(tempQ.pop() != thisString[counter]):
        return False
      counter += 1
      
  return True


if __name__ == '__main__':
  myQueue = Deque()
  myQueue.push_front(1)
  myQueue.push(9)
  myQueue.push(10)
  myQueue.push(11)
  myQueue.push(12)
  myQueue.push(13)
  myQueue.push(14)
  myQueue.push(15)
  myQueue.push(16)
  myQueue.push(17)
  myQueue.push(18)
  myQueue.push(19)
  myQueue.push(20)
  myQueue.push(21)
  myQueue.push(22)
  myQueue.push_front(999)
  myQueue.push_front(200)
  print(myQueue.peek_front())
  myQueue.pop_front()

  print(myQueue.peek())
  myQueue.pop()
  print(myQueue.peek())

 
  while(not(myQueue.empty())):
    myQueue.pop()
  
  print(myQueue.peek())
  print(myQueue.size)

  print(is_palinddrome("racecar"))
  print(is_palinddrome("hello"))

  #for i in range(myQueue.capacity):
   # print (myQueue.array[i])