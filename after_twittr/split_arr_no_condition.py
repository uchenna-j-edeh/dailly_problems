"""Given a list [2,3,10,9,8,4,5,7,6]. return true if the entire array can be split in half
"""

def helper(arr, n, start, rsum, lsum):
    if start == n:
        print(f"ensing it here left:{lsum} right: {rsum}")
        return lsum == rsum

    return helper(arr, n, start+1, rsum + arr[start], lsum + arr[start]) #and helper(arr, n, start+1, rsum, lsum + arr[start])

def split_arr(arr, n):
    return helper(arr, n, 0, 0, 0) # arr, len, start, lsum, rsum

if __name__ == "__main__":
    # arr = [1,4,3]
    arr = [2,3,10,9,8,4,5,7,6]
    n = len(arr)
    if split_arr(arr, n):
        print("Yes")
    else:
        print("No")