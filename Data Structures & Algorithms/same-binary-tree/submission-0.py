# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node, res):
    if(node == None):
        res.append(-1)
        return res
    traversal(node.left, res)
    traversal(node.right, res)
    res.append(node.val)
    return res

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_one = traversal(p,[])
        tree_two = traversal(q,[])
        print(tree_one)
        print(tree_two)
        if(tree_one == tree_two):
            return True
        return False