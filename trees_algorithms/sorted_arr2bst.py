# given a list of sorted arrays, build a BT


class Node:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

def sorted_list_2_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = Node(nums[mid])

    root.left = sorted_list_2_bst(nums[:mid])
    root.right = sorted_list_2_bst(nums[mid+1:])

    return root




nums = [1,2,3,4,5,6,7]
root = sorted_list_2_bst(nums)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.right.val)
print(root.right.left.val)
print(root.left.right.val)
print(root.left.left.val)