#Author: Harrison Reed
#Date 9/25/2023
#Description: Part two to lab 4, implementing word to deque, Off by one, Off by n

from EECS330_Lab4_PartA_LinkedList import Deque

#loop through each char in the string and push it to the queue
def wordToDeque(input):
    myDeque = Deque()

    for i in range(len(input)):
        myDeque.push(input[i])
    
    return myDeque
    pass

#Test for word to deque
def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front == None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True
test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque)) # Should return True

#Using deque find if two chars are next to each other in the alphabet
def OffByOne(char1, char2):
    myAlphabet = Deque()
    for i in range(97,123):
        myAlphabet.push(chr(i))

    prev = ""

    while(myAlphabet.Front() != char2):
        prev = myAlphabet.Front()
        myAlphabet.pop_front()
    myAlphabet.pop_front()

    if(prev == char1 or myAlphabet.Front() == char1):
        return True
    else:
        return False

#Using the integer values of the chars see if char1 + or - N is equal to the integer value of char 2
#If so return true, else return false    
def OffByN(char1, char2, N):
    if(ord(char1) + N == ord(char2)):
        return True
    if(ord(char1) - N == ord(char2)):
        return True
    
    return False

if __name__ == '__main__':
   
   #Testing word to deque 
   myWord = wordToDeque("Hello")
   testWordToDeque("Hello" , myWord)

   #Testing off by one
   print("Testing a and b off by 1: ", OffByOne('a', 'b'))
   print("Testing g and f off by 1: ", OffByOne('g', 'f'))
   print("Testing a and h off by 1: ", OffByOne('a', 'h'))
   print("Testing z and a off by 1: ", OffByOne('z', 'a'))

   #Testing off by N
   print("Testing a and d off by 3: " , OffByN('a', 'd', 3))
   print("Testing h and e off by 3: ", OffByN('h', 'e', 3))
   print("Testing a and a off by 3: ", OffByN('a', 'a', 3))
   print("Testing y and z off by 3: ", OffByN('y', 'z', 3))

   char1 = 'b'
   char2 = 'e'
   N = 3
   print("Testing b and e off by 3: ", OffByN(char1, char2, N)) #Prints True