"""
This is a brute force algo with running time of O(N^2)
asymptotic complexity O(N^2)
A = [9,1,5,6,3,4,9,0]
"""

class Solution:
    def selection_sort(self, A):
        for i in range(len(A)):
            min = i
            #import pdb; pdb.set_trace()
            for j in range(i+1, len(A)):
                if A[j] < A[min]:
                    min = j 

            if i == min: continue
            print("Switched {} with {}".format(A[i], A[j]))
            temp = A[min]
            A[min] = A[i]
            A[i] = temp

        return A
sol = Solution()

A = [9,1,5,6,3,4,9,0]
print("The solution is: ", sol.selection_sort(A))

