"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from pprint import pprint as pp

class Solution:
    def generate(self, numRows):
        pas_tri = []
        for i in range(numRows):
            if i == 0:
                pas_tri.append([1])
                continue

            if i == 1:
                pas_tri.append([1, 1])
                continue

            previous = pas_tri[i-1]
            new_list = [1]
            len_prev = len(previous)
            for j in range(len_prev):
                if j + 1 < len_prev: 
                    new_list.append(previous[j] + previous[j+1])

            new_list.append(1)
            pas_tri.append(new_list)

        return pas_tri
    
sol = Solution()
print("The solution is: ", pp(sol.generate(5)))
print("The solution is: ", pp(sol.generate(15)))
print(sol.generate(20))



