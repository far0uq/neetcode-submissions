# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inOrderTraversal(node):
    if(node == None):
        return
    
    inOrderTraversal(node.left)
    inOrderTraversal(node.right)
    intermediary = node.left
    node.left = node.right
    node.right = intermediary

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inOrderTraversal(root)
        return root
        
        