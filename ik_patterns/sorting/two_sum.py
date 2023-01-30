"""example: given [2,7,1,9] with target 8, return (7,1)
given [3,9,5,5] with target 10 return (5,5)
    """


def two_sum_classic(arr, target):
    mdict = {}
    for a in arr:
        diff = target - a # 8-2 = 6 -> False| 8-7=1, 8-7=1
        if mdict.get(diff, False): # true if key exists|False|False|True
            return (a, diff) # or if index is needed create loop variable and use it | (1, diff)

        mdict[a] = 1 # {2:1}|{2:1, 7:1}

    return None
            

print(two_sum_classic([2,7,1,9], 8))
print(two_sum_classic([3,9,5,5], 10))

def two_sum_index(arr, target):
    mdict = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if mdict.get(diff, False):
            # print(mdict)
            return (mdict[diff] - 1, i)

        mdict[arr[i]] = i + 1 # so we avoid index 0 which is false



print(two_sum_index([2,7,1,9], 8))
print(two_sum_index([3,9,5,5], 10))
print(two_sum_index([3,9,5,5], 8))