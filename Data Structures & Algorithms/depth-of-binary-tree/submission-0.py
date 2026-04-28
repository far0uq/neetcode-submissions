# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node,depth=0):
    if(node == None):
        return depth
    return max(traversal(node.left,depth+1),traversal(node.right,depth+1))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return traversal(root)
        