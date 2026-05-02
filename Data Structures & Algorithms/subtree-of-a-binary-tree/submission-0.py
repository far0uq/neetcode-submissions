# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node,res):
    if(node == None):
        res.append(-1)
        return res
    traversal(node.left,res)
    traversal(node.right,res)
    res.append(node.val)
    return res

def isSubstring(arr1,arr2):
    if(arr2 in arr1):
        return True
    return False


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr1 = traversal(root,[])
        arr2 = traversal(subRoot,[])
        return isSubstring(str(arr1)[1:-1],str(arr2)[1:-1])