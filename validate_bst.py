# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
arr = []
inlen = 0

def checkBST(root):
    global arr
    if root is None:
        return True
    if checkBST(root.left):
        arr.append(root.data)
        if len(arr)>=2:
            if arr[-1]>arr[-2]:
                return True and checkBST(root.right)
            else:
                return False
        else:
            return checkBST(root.right)
    else:
        return False
        
        

# def checkBST(root):
#     if root.left is None and root.right is None:
#         return True
#     elif root.left is None and root.data <= root.right.data:
#         return checkBST(root.right)
#     elif root.right is None and root.data >= root.left.data:
#         return checkBST(root.left)
#     elif root.left.data <= root.data <= root.right.data:
#         return checkBST(root.left) and checkBST(root.right)
#     else:
#         return False
