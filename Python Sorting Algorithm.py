# Python:  2.7.11
#
# Author:  Michael Harrison
#
# Version: 1.1
#
# Purpose: Develop a sorting algorithm to sort a list of integers
#
#


#SORT USING SELECTION SORT ALGORITHM

def selectionSort(numList):
    for sortSlot in range(len(numList)-1,0,-1):
        positionOfMax = 0
        for location in range(1,sortSlot+1):
            if numList[location] > numList[positionOfMax]:
                positionOfMax = location

        temp = numList[sortSlot]
        numList[sortSlot] = numList[positionOfMax]
        numList[positionOfMax] = temp

numList = [67, 45, 2, 13, 1, 998]
selectionSort(numList)
print(numList)


#SORT USING INSERTION SORT ALGORITHM

def insertionSort(numList):
    for index in range(1,len(numList)):

        currentValue = numList[index]
        position = index

        while position > 0 and numList[position-1] > currentValue:
            numList[position] = numList[position-1]
            position = position-1

        numList[position]=currentValue

numList = [89, 23, 33, 45, 10, 12, 45, 45, 45]
insertionSort(numList)
print(numList)
