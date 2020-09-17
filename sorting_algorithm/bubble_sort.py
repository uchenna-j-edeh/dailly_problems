"""
This is a brute force algo with running time of O(N^2)
asymptotic complexity O(N^2)
A = [9,1,5,6,3,4,9,0]
"""

class Solution:
    def bubble_sort(self, A):
        for i in range(len(A)):
            for j in reversed(range(i, len(A))):
                #print(j)
                if A[j] < A[j-1]:
                    temp = A[j-1]
                    A[j-1] = A[j]
                    A[j] = temp

    
        return A
    
sol = Solution()
A = [9,1,5,6,3,4,9,0]
print("The solution is: ", sol.bubble_sort(A))

