import math
from random import randint, seed
import statistics
import time
import sys

#Name: Lab11.py
#Description: Program for EECS3330 Lab, that implements the Quick Sort Algorithm, and Radix Sort Algorithm
#Author: Harrison Reed
#Date:12/1/2023
#Input: Gets input from user for selecting which sort to test
#Output: Prints the list to be sorted, then the sorted list, and the time it took to sort the list

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty arr
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    #Name:quicksort
    #Description: Recursive/Driver function for the partition elemet of QS
    #Input: low- lower bound, high- upper bound. to be sorted
    #Output: None
    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            if(pi != None): # Partitioning index
                self.quicksort(low, pi-1)  # Recursively sort elements before partition
                self.quicksort(pi+1, high)  # Recursively sort elements after partition

    #Name: partition
    #Description: Moves elements in a list(Inplace), to the left if less than or equal to chosen pivot, or right if greater than
    #Input: low- lower bound, high- upper bound. to be partitioned
    def partition(self, low, high):
        #Get pivot value based on median of [low,middle,high]
        #This is done to avoid worst case secnarios(i.e pivot is smallest or largest element in array)
        pivot = self.median_of_three(low,high)

        #Case where the given sub array is already sorted, this is added to increase efficency
        #When lists are large, but there are numerous counts of the same number
        if(isSorted(self.arr[low:high+1])):
            return

        #Set i = low value(Start of the subarray)
        i = low
        #While we are checking values contained in the subarray
        while i < high + 1 :
            #If i == to pivot then we increase i and continue. Since the pivot should not be moved directly
            if(i == pivot):
                i += 1
                continue
            
            #If item at i is <= item at pivot
            if(self.arr[i] <= self.arr[pivot]):
                #Then if i < pivot, it is already on the right side of the pivot
                #So we can increment i and continue
                if(i < pivot):
                    i += 1
                    continue
                #If not then remove item from array
                else:
                    temp = self.arr.pop(i)
                    #Then insert it at the low end of the array, so its on the right side of the pivot
                    self.arr.insert(low, temp)
                    #Increase pivot value since we are inserting at the front of the(Pivot = 4,Index of pivot = 2, [1,2,4,3] -> [3,1,2,4], index of pivot = 3)
                    pivot += 1
                    #Decrement i since we are removing item at i, which means i + 1 -> i, so we must update i to check i + 1 
                    i -= 1

            #Now check the case where item at i is greater than item at pivot
            elif(self.arr[i] > self.arr[pivot]):
                #Same case where item at i is already on right side of the pivot
                if(i > pivot):
                    i += 1
                    continue
                else:
                    #Else remove item and insert it to the right of the pivot
                    temp = self.arr.pop(i)
                    self.arr.insert(high, temp)
                    #In this case we need to decrement the pivot since we are inserting at the end of the array
                    #Pivot = 4, index of pivot = 3, [5,1,2,4] - > [1,2,4,5], index of pivot = 2
                    pivot -= 1
                    #Note no need to update i here since we are inserting at the end of the array therefore in memory array will look like
                    #[5,1,2,4] -> [_,1,2,4,5]
                   
            
        #Return the pivot value after partitioning
        return pivot
        pass  
    
    #Name: median_of_three
    #Description: returns the index of the median number at index for low,middle,high
    #Input: low, high
    #Output: returns the median of three numbers 
    def median_of_three(self, low, high):
        middle = self.arr[math.floor(high/2)]#Get middle value
        thisLow = self.arr[low]#Get low value
        thisHigh = self.arr[high]#Get high value

        temp = [[thisLow, low], [middle, math.floor(high/2)], [thisHigh,high]]#2d array with folowing, [[index],index]
        thisMed = statistics.median(temp)#Get median
        return thisMed[1]#Return index

        pass

#Name: getNumAtPos
#Description: Gets the digit associated with which posistion its in(i.e 1's, 10's, 100's)
#Input:num(The full number), pos(The posistion to get the digit)
def getNumAtPos( num, pos):
    #Get posistion in 0,1,2,3 from 10's
    thisPos = math.ceil((math.log(pos, 10)))
    #Convert num to string
    strNum = str(num)
    #if the length of the string is < the posistion being requested. Then the num is one 10's lower then pos
    #i.e if pos is 10 and num is 1's then we return 0 
    if(len(strNum) < thisPos + 1):
        return 0
    
    #Reverse the string since String[0] returns the first element in string 3241 = 3, -> 1423 = 1
    strNum = strNum[::-1]
    #Get the num at posistion 
    result = strNum[int(thisPos)]
    #Return the strnum as int
    return int(result)

#Name: counting_sort
#Description: Sorts items based on which posisition in digit
#Input: arr-array to be sorted, exp-which posistion to sort from
#Output: None
def counting_sort( arr, exp):
    #Create array of 0, size 10, since we dont know the count of digits(0-9) yet
    myCount = [0]*10
    # Count occurrences of each digit.
    for i in range(len(arr)):
        temp = getNumAtPos(arr[i], exp)
        myCount[temp] += 1
    # Update count to store the position of the next occurrence.
    for i in range(1, len(myCount)):
        #This allows us to insert items into array, in correct order, even if there are mutiple of the same item
        myCount[i] += myCount[i - 1]

    # Build the output array.
    #Create a copy of arr
    #This is done so the original arr is sorted, since we don't return an array
    tempArr = arr.copy()

    #Start at the back of the array
    #This is done so that when sort based on items with pos > 1. They don't become reversed
    i = len(arr) - 1
    #Go through entire array
    while i >= 0:
        #Get item to be moved in the array
        temp = tempArr[i]
        #Get the posistion that they need to be moved to in array
        pos = myCount[getNumAtPos(temp, exp)]
        #Update the original arr with the number to be moved
        arr[pos - 1] = temp
        #Update counts posistion so that we dont have collision of items
        myCount[getNumAtPos(temp, exp)] -= 1 #Update counts posisition
        #decrement i
        i -= 1

    pass

#Name: radix_sort
#Description: sorts an array using the radix sort algorithm
#Input: arr
def radix_sort(arr):
    # Return if array is empty.
    if(len(arr) == 0):
        return
    #Get start time
    start = time.process_time()
    
    #Print array before sort
    print()
    print("Array to be sorted: ", arr)

    # Find the maximum number to know the number of digits.
    max_num = max(arr)
    # Do counting sort for every digit.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    #Get the end time
    end = time.process_time()
    #Print sorted array
    print("Sorted Array: ", arr)
    #Print the time it took
    print("Sorted in: ", end - start)
    print()
    pass
    

# Test quick sorting technique
def isSorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False
def is_sorted(arr):
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"


def test_quicksort():
    """Test the Quicksort algorithm"""
    seed_num = 43   
    seed(seed_num)  # Set the seed for reproducibility
    sorting = Sorting(10)
    for _ in range(10):
        sorting.add(randint(1, 100))
    start = time.process_time()
    print("Array to be sorted: ",sorting.arr)
    sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
    print("Sorted Array: ",sorting.arr)
    end = time.process_time()
    print("Quick Sort:", is_sorted(sorting.arr))
    thisTime  = end - start
    print("Sorted in ", thisTime)

# Test radix sorting technique
def test_radix_sort():
    # Test case 1
    arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
    radix_sort(arr1)
    assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

    # Test case 2
    arr2 = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(arr2)
    assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

    # Test case 3
    arr3 = [1, 200, 3, 400, 5]
    radix_sort(arr3)
    assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

    # Test case 4 (empty array)
    arr4 = []
    radix_sort(arr4)
    assert arr4 == [], f"Test case 4 failed: {arr4}"

    # Test case 5 (array with one element)
    arr5 = [42]
    radix_sort(arr5)
    assert arr5 == [42], f"Test case 5 failed: {arr5}"

    print("All test cases passed!")

if __name__ =='__main__':
    while(True):
        myIn = int(input("1. Quick Sort\n2. Radix Sort\n3. Exit\n\nSelect Sorting Algorithm to test: "))
        print("\n------------------------------------------")
        if(myIn == 1):
            test_quicksort()
            print("------------------------------------------")
        if(myIn == 2):
            test_radix_sort()
            print("------------------------------------------")
        if(myIn == 3):
            break
    pass