"""
Given the following arrays, write a heapsort algo to sort it
A = [9, 1, 5, 6, 3, 4, 9, 0, 20]
"""
class HeapSort:
    def __init__(self):
        self.arr = [-1]
        self.idx = 0

    def add_node(self, elem):
        if self.idx == 1: # build root
            self.arr.append(elem)
            self.idx = self.idx + 1
            return

        self.idx = self.idx + 1
        self.arr.append(elem)
        self.add_node_helper( self.idx)

    def add_node_helper(self, i):
        if i == 1:
            return

        p_index = 0
        if i % 2:
            p_index = (i - 1) // 2
        else:
            p_index = i // 2

        print("parent index is ", i, self.arr, p_index)
        if self.arr[p_index] < self.arr[i]:
            self.arr[p_index], self.arr[i] = self.arr[i], self.arr[p_index]
            self.add_node_helper(p_index)
        return

    def find_max(self):
        max_index = self.arr[1]
        self.arr[i]
        self.idx = self.idx - 1


    
        

A = [9, 1, 5, 6, 3, 4, 9, 0, 20]

HS = HeapSort()
for i in A:
    HS.add_node(i)

print(HS.arr)

