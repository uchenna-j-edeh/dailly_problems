"""
Write a function that returns the number of distinct binary search trees that can be constructed with n nodes.

For the purpose of this exercise, do solve the problem using recursion first even if you see some non-recursive approaches.



Example One

Input: 1



Output: 1



Example Two

Input: 2



Output: 2



Suppose the values are 1 and 2, then the two trees that are possible are

   (2)               (1)

  /          and       \

(1)                     (2)

"""

def helper(n, i, slate):
    # bsae case
    if len(n) == 1:
        return 1
    if len(n) == 2:
        return 2
    if i == len(n):
        return 1
    
    return helper(n, i+1, slate) + helper(n, i+1, slate+[n[i]])
def how_many_BSTs(n):
    nodes = ""
    for i in range(n):
       nodes = nodes + str(i+1) 
    print(nodes)
    return helper(nodes, 0, [])

print(how_many_BSTs(5))
print(how_many_BSTs(3))
    

