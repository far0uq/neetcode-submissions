# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node):
    if (node == None):
        return [0,0]
    left = traversal(node.left)
    right = traversal(node.right)
    diameter = left[0] + right[0]
    deepest_child = max(right[0], left[0])
    max_child_depth = max(left[1], right[1])
    return [deepest_child + 1, max(diameter, max_child_depth)]    

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        myarray = traversal(root)
        return myarray[1]
        