"""
      a
     / \
    b   c
  /  \   \
d      e  f
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def buildTree(a,b,c,d,e,f):
    # root node
    root = Node(a)    
    root.left = Node(b)
    root.right = Node(c)
    # left child of root
    root.left.left = Node(d)
    root.left.right = Node(e)
    # right child of root
    root.right.right = Node(f)

    return root


counter = 0
def is_uval(root):    
    global counter
    if root is None:
        return True

    left_leaf = is_uval(root.left)
    right_leaf = is_uval(root.right)
   
    if not left_leaf or not right_leaf:
        return False

    if root.left is not None and root.left.val != root.val:
        return False

    if root.right is not None and root.right.val != root.val:
        return False
    
    counter = counter + 1
    print(counter)
    return True
    

root = buildTree(5,5,5,5,5,5)
def findSingleValueTrees(root):
    is_uval(root)
    return counter

print(findSingleValueTrees(root))
