"""
Must maintain heap order property. For every node x with parent p, the key in p is smaller than or equal to the key in x
[0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
cpmplete tree:
i. We can represent usint a list
ii. No need to use nodes and references
iii. Left child of a parent (at position p) is the node that is found in position 2p
iv. Right child of the parent is at position 2p+1 in the list
"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while(i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1] # first element in array
        self.heapList[1] = self.heapList[self.currentSize] # to maintain order, swap the first element in array with last
        self.currentSize = self.currentSize - 1 # reduce size by 1
        self.heapList.pop() # remove the last element since its now the root element
        self.percDown(1)
        return retval



    def buildHeap(self, alist):
        #global alist
        i = len(alist) // 2 # start in the middle. The largest child is always moved down the tree, afterall the tree is complete binary tree, any nodes past the halfway will be leaves and therefore have not children
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:] # copy old list onto new list padding new list with first element that is 0
        while (i > 0):
            self.percDown(i)
            i = i - 1 # starts at middle and work your way up.
        return self.heapList
            
        

alist = [9, 5, 6, 2, 3]     
BH = BinHeap()

print(BH.buildHeap(alist))

#print(alist)

