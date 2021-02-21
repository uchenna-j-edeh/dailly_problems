"""
Given an array of in, find all group of three numbers whose sum is 0
"""

def findZeroSum(arr):
    # Write your code here.
    seen = dict()
    seen_index = dict()
    for k in range(len(arr)): # put all values in dict using index as key shifted by 1 becasue of 0 index
        seen[arr[k]] = k + 1
    
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            val = 0 - (arr[i] + arr[j])
            if seen.get(val, False):
                k = seen[val] - 1
                values = tuple(sorted([arr[i], arr[j], arr[k]]))
                if  not seen_index.get(values, False) and k not in [i,j]:
                    result.append("{},{},{}".format(arr[i], arr[j], arr[k]))
                    seen_index[values] = 1
    return result

#def findZeroSum_v2(arr):
#    sl = sorted(arr)
#    for i in len(arr):
#        for 

print(findZeroSum([10, 3, -4, 1, -6, 9]))
