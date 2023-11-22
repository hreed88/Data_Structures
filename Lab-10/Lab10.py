#Name: Lab10.py
#Author: Harrison Reed
#Date: 11/21/2023
#Description: Program for EECS 330 Lab 10 that implements Selection, Heap, and Merge Sort

import math
import time
from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

  #Name: Selection_Sort
  #Description: Selection Sorting algorithm to sort a list in O(n^2) on average
    def selection_sort(self):
        #Outer Loop for the current item we compare to the rest of the list
        for i in range(len(self.arr)):
           #Set current item and smallest item to the same 
           currItem = self.arr[i]
           smallestItem = self.arr[i]
           #Keep track of current index
           currIndex = i
           #Inner loop where we only care about i + 1 items, becuase 0-i is sorted
           for j in range(i + 1, len(self.arr)):
              #If we find a smaller item set that = to smallest item and update curr index
              if smallestItem > self.arr[j]:
                smallestItem = self.arr[j]
                currIndex = j
           #If we find a new smaller item swap the item at i and new index
           if currIndex != i:
            self.arr[i] = smallestItem
            self.arr[currIndex] = currItem
        pass
    
    
    #Name: max_heapify
    #Description: Helper function for heap_sort, in which it creates a max heap based on given index for a list
    def max_heapify(self, n, i):
      #current root is max
      max = i
      #left and right child based on tree structure for list
      leftChild = i * 2 + 1
      rightChild = i * 2 + 2

      #if the left child is higher on the tree than n and if it is greater than its parent, update the max value
      if(leftChild < n and self.arr[leftChild] > self.arr[max]):
         max = leftChild
      #Do the same for the right child
      if(rightChild < n and self.arr[rightChild] > self.arr[max]):
         max = rightChild

      #If we find that one of the children is greater than its parent than perform a swap, updating the heap
      if(max != i):
         temp = self.arr[i]
         self.arr[i] = self.arr[max]
         self.arr[max] = temp
         
         #Repeat if we updated max, as we probably need to keep updating the heap
         self.max_heapify(n, max)
      pass

    
    #Name: Heap_sort
    #Description: Heap sorting algorithm, to sort lists in O(nlog(N)) time
    def heap_sort(self):
       #Get the length of the array, as we want to move up the tree
       n = len(self.arr)
       #Since each level of the tree will be k/2,where k is the current length of subtree, we just need to traverse n/2
       for i in range(int((n / 2) - 1), -1, -1):
          #Create max heap
          self.max_heapify(n, i)
       
       #From max heap move item at 0, which is root, to the back of the list
       for i in range(n - 1, -1, -1):
          temp = self.arr[0]
          self.arr[0] = self.arr[i]
          self.arr[i] = temp
          #Create max heap from new item at the front of the list
          self.max_heapify(i, 0)

       pass
    
    #Name: mergeSort
    #Description: Merge sorting algorithm, to sort lists in O(nlog(N)) time
    def mergeSort(self):
       #Calls recursive algorithm
       self.arr = self.mergeHelper(self.arr)
       pass
    #Name: Merge
    #Descripton: Merges two arrays, while also sorting them
    def merge(self, arr1, arr2):
       #Sorted list
       tempList = []
       #Indicies for array 1 and 2
       i = 0
       j = 0

      #Used to check if we have already gotten through one of the sub arrays
       endOfList1 = False
       endOfList2 = False
      #Loops until i and j are both == the size of their arrays
       while(j < len(arr2) or i < len(arr1)): 
        #Case where we have already comapred all of list 1
        #We just add on the rest of list 2
        if(endOfList1):
           tempList = tempList + arr2[j: len(arr2)]
           break
        #Same for list 2
        if(endOfList2):
           tempList = tempList + arr1[i: len(arr1)]
           break
        
        #Compare current indicies for array 1 and 2
        if(arr1[i] < arr2[j]):
           #If the item at i is less than item at j,
           #Then add it to the end of tempList
           tempList.insert(len(tempList), arr1[i])
           #And increment i
           i += 1
           #If i is == to the len of arr1, then we have completed list 1
           if(i == len(arr1)):
              endOfList1 = True
        #If i is greater than j than we add the item at j and increament j
        else:
           tempList.insert(len(tempList), arr2[j])
           j += 1
           if(j == len(arr2)):
              endOfList2 = True

       return tempList 
    
    #Name: Merge Helper
    #Description: Recursive helper function for Merge sort
    def mergeHelper(self, subArr):
        
        splitInd = None
        tempList = []

        #Base case
        #If there is only 1 item we can return the array
        if(len(subArr) == 1):
            return subArr

        #Else we need to find where we want to split the array
        if(len(subArr) % 2 != 0):
            #If the size of the array is odd, then we take the floor of n/2
            splitInd = math.floor(len(subArr) / 2)
        else:
            #If not we can just take n/2
            splitInd = int(len(subArr) / 2)

        #Split the arrays based of splitInd
        leftArr = subArr[0:splitInd]
        rightArr = subArr[splitInd:len(subArr)]

        #Recursive call on the left and right arrays
        temp1 = self.mergeHelper(leftArr)
        temp2 = self.mergeHelper(rightArr)

        #Merge the two sub arrays
        tempList = self.merge(temp1, temp2)
        
        #Return the merged list
        return tempList
        pass
      
    #Name: test_sorting_time
    #Description: Calculates the time it takes to sort arrays of size n, where we can select which algorithm to use
    def test_sorting_time(self, sorting_method):
      start_time = time.process_time()
      if(sorting_method == "selection"):
         self.selection_sort()
      if(sorting_method == "heap"):
         self.heap_sort()
      if(sorting_method == "merge"):
         self.mergeSort()

      end_time = time.process_time()

      #Return the proccesor clock after the array is sorted - the processor clock before the array is sorted
      return end_time - start_time
      pass

#Test Sorted array
def is_sorted(arr):
  if arr == sorted(arr):
    return ("Passed!")
  else:
    return ("Failed!")

# Test each sirting technique
def test_sort_algorithms(sorting_method, set_seed=None):
  if seed != None:
    seed(set_seed)
  sorting = Sorting(10)
  # Add 10 random elements
  for _ in range(10):
    sorting.add(randint(1, 100))
  # Apply the sorting algorithm
  if sorting_method == 'selection':
    print("\nBefore Sort:", sorting.arr)
    sorting.selection_sort()
    print("After Sort:", sorting.arr)
    print("Selection Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'heap':
    print("\nBefore Sort:" , sorting.arr)
    sorting.heap_sort()
    print("Aftert Sort:" , sorting.arr)
    print("Heap Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'merge':
    print("\nBefore Sort:" , sorting.arr)
    sorting.mergeSort()
    print("After Sort:" , sorting.arr)
    print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
  seeding = 45
  array_sizes = [10000,20000,30000,40000,50000]
  methods = ['selection', 'heap', 'merge']
  print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
  for size in array_sizes: 
    times = []
    for m in methods:
      sorting = Sorting(size)
      seed(seeding)
      for _ in range(size):
        sorting.add(randint(1, 50000))
      interval = sorting.test_sorting_time(m)
      times.append(interval)
    print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")

if __name__ == '__main__':
  seed_num = 43   
  test_sort_algorithms('selection', seed_num)
  test_sort_algorithms('heap', seed_num)
  test_sort_algorithms('merge', seed_num)
  run_time_tests()

  #B2
  #Time Complexity
  #
  #Selection Sort
  #Complexity O(n^2) - Average
  #What O(n^2) means that based on the input size N the time will scale exponitaly
  #Why is this? This is because in the algorithm for selection sort we must make n^2 comparisons
  #This is based off of the inner and outer loops, where for each item we must compare it to every other item in the list
  #(Exluding every item that is already sorted, i.e j = i + 1)
  #
  #
  #Heap Sort
  #Complexity O(n*log(n)) - Average
  #What O(n*log(n)) means that based on input size time will scale at a linear * logarithmic rate
  #Why is this? For each root node we are taking the subtree and making the sub tree a max heap
  #Where taking the sub tree will be on average n/2(Where n is the current subtree) giving us log(n)
  #And where in each subtree we must make N comparisons(Heapifiying) giving us n, which in turn gives us O(nlog(n))
  #
  #
  #Merge Sort
  #Complexity O(n*log(n)) - Average
  #What O(n*log(n)) means that based on input size time will scale at a linear * logarithmic rate
  #Why is this? Because Merge sort is a recursive algoritm, where in general we split the array into 2 n/2 sized arrays
  #All the way down until we have sub Arrays of size 1, giving us the log(n)
  #Then we begin are way "Back Up" where we merge the sub arrays of sizes 1,2,3,...,n/2
  #In Which each merge we must make k comparisons where k = (Sub Array 1's length + Sub Array 2's Length)
  #Where the final merge will be of size N, giving us N, so with these two operations we get O(N*log(N))
  #(Note - Merge sort generally has a faster running time even though both are O(Nlog(N))
  
