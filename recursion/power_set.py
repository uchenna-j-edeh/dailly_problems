"""
print power set
"""

def power_set_helper(nums, i, result, slate):
    if i == len(nums):
        result.append(slate)
        return

    power_set_helper(nums, i + 1, result, slate + str(nums[i])) # include case
    power_set_helper(nums, i + 1, result, slate) # exclude case

def power_set(nums):
    result = []
    power_set_helper(nums, 0, result, "")
    return result

print(power_set([1,2,3]))
print(power_set([1,2,3,4]))

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ...n.
Example:
    input: n = 4, k=2
    output: [ [2,4], [3,4], [2,3], [1, 2], [1,3], [1,4] ]
"""
result = []

def sub_helper(n, i, k, slate):
    # backtrack case:
    if len(slate) == k:
        result.append(slate[:])
        return

    #base case
    #if i == n+1:
    if i == len(n):
        return

    #recursive case
    #exclude
    sub_helper(n, i+1, k, slate)
    #include i
    slate.append(i)
    sub_helper(n, i+1, k, slate)
    slate.pop()

def sub_power_set(n, k):
    sub_helper(n, 0, k, [])
    return result

print(sub_power_set([1,2,3,4], 2))
print(sub_power_set([1,2,3,4], 3))


result = []
def im_helper(n, i, slate):
    #base case
    if i ==len(n):
        result.append(slate[:])
        return
    #recursive case
    #exclude
    im_helper(n, i+1, slate)

    #include case
    slate.append(n[i])
    im_helper(n, i+1, slate)
    slate.pop()


def immut_power_set(n):
    im_helper(n, 0, [])
    return result

print(immut_power_set([5,6,7,8]))
