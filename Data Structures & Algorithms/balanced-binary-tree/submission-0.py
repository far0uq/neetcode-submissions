# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node, depth=0):
    if(node == None):
        return [True,depth]
    left = traversal(node.left, depth+1)
    right = traversal(node.right, depth+1)
    if(left[0] and right[0]):
        if(abs(left[1] - right[1]) < 2):
            return [True,max(left[1],right[1])]
        else:   
            return [False, max(left[1],right[1])]
    else:
        return [False, max(left[1],right[1])]
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = traversal(root)
        return res[0]