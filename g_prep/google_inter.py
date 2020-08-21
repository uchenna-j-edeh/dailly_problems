"""
0, 1, 1, 0, 1, 1, 0, 1, 1

Pisano(A, B, M) → [A,B, (A+B)%M …. ] continue until repetition.

Pisano(0, 1, 3) → [0, 1, 1, 2, 0, 2, 2, 1]


Modulus 4
5,6 →  3
2,4 → 2


Modulus 4
0,1,1,2,3,1,0,1

--->   [0,1,1,2,3,1]  the objective is to find the list of elements until repetition

Sounds good.
"""
aList = [1,4, 5, 7, 2, 3, 1]
newList = [1, 25, 49, 9, 1]

def square_odd(aList):
    newList = []
    for i in aList:
        if i % 2:
            newList.append(i)
    return newList



def solution(A, B, M):
    aList = [A, B]
    i = 0    
    while True:
        aList.append( (aList[i] + aList[i+1]) % M ) # [A, B, C]
        if (A == aList[i+1] and B == aList[i+2]):
             return aList
        i = i + 1
        
print("The solution is: ", solution(0, 1, 2))
print("The solution is: ", solution(0, 1, 3))
print("The solution is: ", solution(1, 2, 3))
print("The solution is: ", solution(0, 1, 4))
print("The solution is: ", solution(3, 2, 4))
print("The solution is: ", solution(2, 3, 4))
print("The solution is: ", solution(0, 1, 5))
print("The solution is: ", solution(3, 4, 5))
print("The solution is: ", solution(4, 5, 6))
print("The solution is: ", solution(5, 4, 6))

